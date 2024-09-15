from fastapi import APIRouter
from app.models.pydantic_models import Query
from app.dependencies import get_vectorstore, get_llm
from app.services.document_retriever import DocumentRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

router = APIRouter()

@router.post("/similarity")
async def similarity_search(query: Query):
    vectorstore = get_vectorstore()
    llm = get_llm()
    
    retriever = DocumentRetriever(vectorstore)
    
    template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    Answer:"""
    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def retrieve_and_format(question):
        docs = retriever.retrieve(question)
        return format_docs(docs)

    rag_chain = (
        {"context": lambda x: retrieve_and_format(x), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    result = rag_chain.invoke(query.question)

    source_docs = retriever.retrieve(query.question)
    
    source_docs_info = [
        {
            "content": doc.page_content,
            "doc_name": doc.metadata.get("doc_name", "Unknown"),
            "chunk_id": doc.metadata.get("chunk_id", "Unknown")
        } for doc in source_docs
    ]

    return {
        "question": query.question,
        "answer": result,
        "source_documents": source_docs_info
    }
from langchain_core.documents import Document

class DocumentRetriever:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def retrieve(self, query: str) -> list[Document]:
        return self.vectorstore.as_retriever().get_relevant_documents(query)
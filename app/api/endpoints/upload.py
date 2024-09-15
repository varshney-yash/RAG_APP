from fastapi import APIRouter, File, UploadFile, HTTPException
from langchain_community.document_loaders import PyPDFLoader
from app.dependencies import get_vectorstore
from app.utils.text_splitter import get_text_splitter

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    
    loader = PyPDFLoader(file.filename)
    pages = loader.load_and_split()
    
    text_splitter = get_text_splitter()
    docs = text_splitter.split_documents(pages)
    
    for i, doc in enumerate(docs):
        doc.metadata["doc_name"] = file.filename
        doc.metadata["chunk_id"] = i
    
    vectorstore = get_vectorstore()
    vectorstore.add_documents(docs)
    
    return {"message": f"File {file.filename} processed and vectors added to Pinecone index successfully"}
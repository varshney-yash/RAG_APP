from pinecone import Pinecone as PineconeClient, ServerlessSpec
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Pinecone
from app.config import PINECONE_API_KEY, PINECONE_INDEX_NAME, GOOGLE_API_KEY

def get_pinecone_client():
    return PineconeClient(api_key=PINECONE_API_KEY)

def get_llm():
    return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

def get_embed_model():
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

def get_vectorstore():
    embed_model = get_embed_model()
    return Pinecone.from_existing_index(PINECONE_INDEX_NAME, embed_model)
from fastapi import FastAPI
from app.api.routes import router
from app.dependencies import get_pinecone_client
from app.config import PINECONE_INDEX_NAME
from pinecone import ServerlessSpec

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    pc = get_pinecone_client()
    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=768,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-west-2'
            )
        )

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

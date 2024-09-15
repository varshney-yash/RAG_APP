from fastapi import APIRouter
from app.api.endpoints import upload, similarity, summarize

router = APIRouter()

router.include_router(upload.router, tags=["upload"])
router.include_router(similarity.router, tags=["similarity"])
router.include_router(summarize.router, tags=["summarize"])
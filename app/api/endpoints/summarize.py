from fastapi import APIRouter
from app.models.pydantic_models import SummarizeRequest
from app.dependencies import get_llm
from app.services.model_handler import ModelHandler

router = APIRouter()

@router.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    llm = get_llm()
    model_handler = ModelHandler(llm)
    summary = model_handler.get_summary(request.text)
    return {"summary": summary}

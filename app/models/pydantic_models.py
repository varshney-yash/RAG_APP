from pydantic import BaseModel

class Query(BaseModel):
    question: str

class SummarizeRequest(BaseModel):
    text: str
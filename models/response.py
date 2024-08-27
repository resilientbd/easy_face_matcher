# app/models/response.py

from pydantic import BaseModel

class CompareResult(BaseModel):
    similarity_percentage: float
    message: str

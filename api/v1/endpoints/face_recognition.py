# app/api/v1/endpoints/face_recognition.py

from fastapi import APIRouter, File, UploadFile, HTTPException
from models.response import CompareResult
from services.face_comparison import compare_faces

router = APIRouter()

@router.post("/compare_faces", response_model=CompareResult)
async def compare_faces_endpoint(
    file1: UploadFile = File(...), file2: UploadFile = File(...)
):
    try:
        similarity_percentage = compare_faces(file1.file, file2.file)
        return CompareResult(
            similarity_percentage=similarity_percentage,
            message="Faces compared successfully."
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred during processing.")

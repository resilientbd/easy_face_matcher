# app/api/v1/__init__.py

from fastapi import APIRouter
from api.v1.endpoints import face_recognition

api_router = APIRouter()
api_router.include_router(face_recognition.router, prefix="/face_recognition", tags=["Face Recognition"])

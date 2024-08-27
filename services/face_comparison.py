# app/services/face_comparison.py

import face_recognition
from fastapi import HTTPException

def compare_faces(img1_data: bytes, img2_data: bytes) -> float:
    # Load the uploaded images
    img1 = face_recognition.load_image_file(img1_data)
    img2 = face_recognition.load_image_file(img2_data)

    # Detect face encodings in both images
    face_encoding1 = face_recognition.face_encodings(img1)
    face_encoding2 = face_recognition.face_encodings(img2)

    if len(face_encoding1) == 0:
        raise HTTPException(status_code=400, detail="No face detected in the first image.")
    if len(face_encoding2) == 0:
        raise HTTPException(status_code=400, detail="No face detected in the second image.")

    # Calculate the face distance between the two faces
    face_distance = face_recognition.face_distance(face_encoding1, face_encoding2[0])[0]

    # Convert face distance to a similarity percentage
    similarity_percentage = (1 - face_distance) * 100
    return round(similarity_percentage, 2)

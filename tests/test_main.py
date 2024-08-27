# tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test the health of the API
def test_api_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is healthy"}

# Test image upload without files (expected failure)
def test_compare_faces_no_images():
    response = client.post("/compare-faces", files={})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"] == "Images are required for comparison."

# Test image upload with only one file (expected failure)
def test_compare_faces_one_image():
    with open("tests/sample_image_1.jpg", "rb") as image1:
        response = client.post("/compare-faces", files={"image1": image1})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"] == "Both images are required for comparison."

# Test image upload with two valid images (expected success)
def test_compare_faces_success():
    with open("tests/sample_image_1.jpg", "rb") as image1, open("tests/sample_image_2.jpg", "rb") as image2:
        response = client.post("/compare-faces", files={"image1": image1, "image2": image2})
    assert response.status_code == 200
    assert "similarity" in response.json()  # Check that similarity is returned
    assert isinstance(response.json()["similarity"], float)  # Ensure it's a float value

# Test handling of images where no face is detected (expected failure)
def test_compare_faces_no_face_detected():
    with open("tests/no_face_image.jpg", "rb") as image1, open("tests/no_face_image.jpg", "rb") as image2:
        response = client.post("/compare-faces", files={"image1": image1, "image2": image2})
    assert response.status_code == 400  # Bad Request
    assert response.json()["detail"] == "Unable to detect face parameters from one or both images."

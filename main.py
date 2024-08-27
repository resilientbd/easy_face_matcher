# app/main.py

from fastapi import FastAPI, HTTPException
from api.v1 import api_router
from exceptions.handlers import http_exception_handler, generic_exception_handler
import uvicorn

app = FastAPI(
    title="Face Recognition API",
    description="An API to compare face similarities between two images.",
    version="1.0.0"
)

app.include_router(api_router)

# Exception handling
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5003,
        reload=True
    )

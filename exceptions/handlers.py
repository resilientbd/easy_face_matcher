# app/exceptions/handlers.py

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": "An internal server error occurred.", "error": str(exc)})

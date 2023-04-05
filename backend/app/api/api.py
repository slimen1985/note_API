from fastapi import APIRouter

from .endpoints.note import note_router

api_router = APIRouter()

api_router.include_router(
    note_router
)
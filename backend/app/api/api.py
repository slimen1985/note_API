from fastapi import APIRouter

from .endpoints.note import note_router
from .endpoints.user import user_router
from .endpoints.home import home_router

api_router = APIRouter()

api_router.include_router(
    note_router
)

api_router.include_router(
    user_router
)

api_router.include_router(
    home_router
)
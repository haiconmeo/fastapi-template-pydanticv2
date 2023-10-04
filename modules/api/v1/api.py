from .endpoints import item

from fastapi import APIRouter
api_router = APIRouter()
api_router.include_router(
    item.router, prefix='/items', tags=["items"]
)

from fastapi import APIRouter
from api.v1.endpoints import members


api_router = APIRouter()
api_router.include_router(members.router)

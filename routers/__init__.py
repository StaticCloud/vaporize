from fastapi import APIRouter
from .userrouter import user_router

router = APIRouter()

router.include_router(user_router, prefix="/user")
from fastapi import APIRouter
from .userrouter import user_router
from .designrouter import design_router

router = APIRouter()

router.include_router(user_router, prefix="/user")
router.include_router(design_router, prefix="/design")
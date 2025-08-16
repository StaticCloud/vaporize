from fastapi import APIRouter
from .bannerrouter import banner_router
from .designrouter import design_router

router = APIRouter()

router.include_router(banner_router, prefix="/banner")
router.include_router(design_router, prefix="/design")
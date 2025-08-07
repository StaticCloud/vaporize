from faspapi import APIRouter
from templaterouter import template_router

template_router = APIRouter()

template_router.include_router(template_router, prefix="/user")
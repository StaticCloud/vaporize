from fastapi import APIRouter
from fastapi.responses import HTMLResponse

template_router = APIRouter()

@template_router.get("/{user_id}", response_class=HTMLResponse)
def get_completed_games(user_id: int):
    pass
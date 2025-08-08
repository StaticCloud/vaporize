from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from steamapi import SteamAPI
from core.template import templates

user_router = APIRouter()

client = SteamAPI()

@user_router.get("/", response_class=HTMLResponse)
def get_completed_games(request: Request, user_id: int):
    if not user_id:
        raise HTTPException(status_code=500, detail=f"Error fetching profile: {str(e)}")
    
    try:
        profile = client.get_player_profile(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching profile: {str(e)}")
    
    if profile is None:
        raise HTTPException(status_code=404, detail="Could not locate a Steam user with the provided id.")
    
    try:
        # temp until body implementation
        games_ids = client.get_completed_game_ids(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching games: {str(e)}")

    return templates.TemplateResponse("partials/_user_data.html", { "request": request, "user": profile })
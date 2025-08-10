from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from core.template import templates
from pydantic import BaseModel;
import json

design_router = APIRouter()

class Payload(BaseModel):
    body: str

@design_router.post("/", response_class=HTMLResponse)
async def post_banner_design(request: Request, payload: Payload):
    body = json.loads(payload.body)
    print(body['banners'])

    payload = {
        "request": request
    }

    return templates.TemplateResponse("partials/_design.html", payload)
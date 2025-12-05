from fastapi.responses import HTMLResponse, RedirectResponse
from db import SessionDep
from fastapi import APIRouter, HTTPException, Request, Form, File, UploadFile
from models import Jugador, JugadorCreate
from sqlmodel import select
from fastapi.templating import Jinja2Templates
from typing import Optional

router = APIRouter()

templates = Jinja2Templates(directory="templates")



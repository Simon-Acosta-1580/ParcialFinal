from fastapi.responses import HTMLResponse, RedirectResponse
from db import SessionDep
from fastapi import APIRouter, HTTPException, Request, Form, File, UploadFile
from models import Jugador, JugadorCreate
from sqlmodel import select
from fastapi.templating import Jinja2Templates
from typing import Optional
from supa.supabase_upload import upload_to_bucket

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/new", response_class=HTMLResponse)
async def show_create(request: Request):
    return templates.TemplateResponse("new_jugador.html", {"request": request})

@router.post("/", response_model=Jugador, status_code=201)
async def create_user(request: Request,
                      session: SessionDep,
                      name: str = Form(...),
                      number: int = Form(...),
                      year: int = Form(...),
                      status: bool = Form(True),
                      img: Optional[UploadFile] = File(None),
                      born: str = Form(...),
                      height: float = Form(...),
                      peso: float = Form(...),
                      pie: str = Form(...),
                      posicion: str = Form(...),
                      valor: float = Form(...),
                      ingreso: int = Form(...),
                      statusFisico: str = Form(...),
                      suspendido: bool = Form(...),
                      ):

    img_url = None
    if img:
        try:
            img_url = await upload_to_bucket(img)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    try:
        new_jugador = JugadorCreate(name=name,
                                    number=number,
                                    year=year,
                                    status=status,
                                    img=img_url,
                                    born=born,
                                    height=height,
                                    peso=peso,
                                    pie=pie,
                                    posicion=posicion,
                                    valor=valor,
                                    ingreso=ingreso,
                                    statusFisico=statusFisico,
                                    suspendido=suspendido
                                    )

        jugador = Jugador.model_validate(new_jugador)
        session.add()
        await session.commit(jugador)
        await session.refresh(jugador)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return RedirectResponse(url=f"/jugador/{jugador.id}", status_code=302)




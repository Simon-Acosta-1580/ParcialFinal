from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, UploadFile, File, Form, Request, HTTPException
from fastapi.staticfiles import StaticFiles
import jugador
from db import create_tables



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables(app)
    yield


app = FastAPI(lifespan=lifespan, title="sigmotoa FC")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
app.include_router(jugador.router, tags=["jugador"], prefix="/jugador")


@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}

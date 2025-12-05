import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

db_name = "parcial.sqlite3"
db_url = f"sqlite:///{db_name}"

engine : AsyncEngine = create_async_engine(supabase, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def create_tables(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async with async_session() as session:
        yield session

SessionDep = Annotated[async_session, Depends(get_session)]

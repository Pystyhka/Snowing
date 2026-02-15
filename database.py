import asyncio
from typing import Annotated
from sqlalchemy import String, create_engine, text, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, DeclarativeBase

from config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)
session_factory = sessionmaker(sync_engine)

class Base(DeclarativeBase):
    pass
# 1.-Load module
import asyncio
from database import engine

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, insert, String
from settings import Settings
# from alchemy import sync_session_factory,sync_engine,async_session_factory
import tables
from tables_New_Create import Base

import requests
import json

sync_engine = create_engine(url=Settings.database_url,
                            # echo=True,
                            pool_size=5,  # основные соеденения
                            max_overflow=10,  # дополнтиленые соеденения
                            )  # ensure this is the correct path for the sqlite file.

async_engine = create_async_engine(url=Settings.database_url,
                                   # echo=True,
                                   pool_size=5,  # основные соеденения
                                   max_overflow=10,  # дополнтиленые соеденения
                                   )  # ensure this is the correct path for the sqlite file.

# async def get_123():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(f"{res.first()=}")
# asyncio.run(get_123())

print("Удаляю таблицы")
Base.metadata.drop_all(engine)

print("Создаю таблицы")
Base.metadata.create_all(engine)

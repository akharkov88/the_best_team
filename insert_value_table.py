from database import engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import URL, create_engine, text, insert, String
from settings import Settings
from  tables import Base

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

def drop_create():
    print("Удаляю таблицы")
    Base.metadata.drop_all(engine)

    print("Создаю таблицы")
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    drop_create()
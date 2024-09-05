from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings
from settings import Settings


engine = create_engine(
    Settings.database_url,
    # connect_args={'check_same_thread': False},
    # echo=True,
    # pool_size=5,  # основные соеденения
    # max_overflow=10,  # дополнтиленые соеденения
)

Session = sessionmaker(
    engine,
    # autocommit=False,
    # autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


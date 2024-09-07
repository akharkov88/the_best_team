from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    DateTime,
    UniqueConstraint,
    Enum,
    Boolean,
)
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
# from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional,Annotated
Base = declarative_base()
from sqlalchemy.orm import Mapped,mapped_column
import datetime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    name= Column(String)
    surname= Column(String)

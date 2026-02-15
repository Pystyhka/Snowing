from sqlalchemy import Table, Column,Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped,mapped_column, relationship
from typing import Annotated
from database import Base
import enum
import datetime

intpk = Annotated[int,mapped_column(primary_key=True)]
created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())"))
    ]

class SnowORM(Base):
    __tablename__ = 'snowing'

    id: Mapped[intpk]
    issnow: Mapped[str]
    created_at: Mapped[created_at]



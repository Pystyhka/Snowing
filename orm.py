import asyncio

from sqlalchemy import Integer, and_, text, insert, inspect, select, func, cast
from database import  sync_engine, session_factory, Base
from sqlalchemy.orm import aliased, joinedload, selectinload
from models import SnowORM
from requests11 import checking_for_snow
import models

class SyncORM():
    @staticmethod
    def create_table():
        Base.metadata.drop_all(sync_engine)
        sync_engine.echo = True
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def snow_is_running():
        with session_factory() as session:
            snowing = checking_for_snow()
            snow_is_coming = SnowORM(issnow=snowing)
            session.add(snow_is_coming)
            session.commit()


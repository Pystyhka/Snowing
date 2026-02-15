import asyncio
import os
import sys
import time
sys.path.insert(1, os.path.join(sys.path[0],'...'))

from orm import SyncORM

#SyncORM.create_table()

while True:
    SyncORM.snow_is_running()
    time.sleep(3600)

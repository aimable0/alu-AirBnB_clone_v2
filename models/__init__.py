#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


from dotenv import find_dotenv, load_dotenv
import os

env_path = find_dotenv(".env")
load_dotenv(env_path)

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()

#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv
# from dotenv import find_dotenv, load_dotenv


# env_path = find_dotenv(".env")
# load_dotenv(env_path)

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()

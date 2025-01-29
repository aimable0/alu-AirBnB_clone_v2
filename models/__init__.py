#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from dotenv import find_dotenv, load_dotenv
from os import getenv

env_path = find_dotenv(".env")
load_dotenv(env_path)

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()

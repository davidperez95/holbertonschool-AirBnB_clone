#!/usr/bin/python3
"""init for the BaseModel class"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

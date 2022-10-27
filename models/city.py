#!/usr/bin/python3
"""Module contains the City class"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """The City class"""
    state_id = ""
    name = ""

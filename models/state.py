#!/usr/bin/python3

"""
This is a file that defines the State Model from the BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """The state class model"""

    # Atr
    name: str = ""

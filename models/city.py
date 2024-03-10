#!/usr/bin/python3

"""
City Model from the BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """city class Model"""

    # Attributes
    name: str = ""
    state_id: str = ""

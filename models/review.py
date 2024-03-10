#!/usr/bin/python3

"""This s the Review Model from the BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class model"""

    # Atr
    place_id: str = ""
    user_id: str = ""
    text: str = ""

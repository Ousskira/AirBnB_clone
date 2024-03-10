#!/usr/bin/python3

"""
This is a file that defines the UserModel class from the BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class model"""

    # Atr
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

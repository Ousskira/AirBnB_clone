#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a User class"""
=======
"""Defines the User class."""
>>>>>>> 4a69549fddf653157ce54a66ecd85339e626c28c
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Class for managing user objects"""
=======
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
>>>>>>> 4a69549fddf653157ce54a66ecd85339e626c28c

    email = ""
    password = ""
    first_name = ""
    last_name = ""

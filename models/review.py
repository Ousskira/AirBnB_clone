#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a Review class"""

=======
"""Defines the Review class."""
>>>>>>> 4a69549fddf653157ce54a66ecd85339e626c28c
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Class for managing review objects"""
=======
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """
>>>>>>> 4a69549fddf653157ce54a66ecd85339e626c28c

    place_id = ""
    user_id = ""
    text = ""

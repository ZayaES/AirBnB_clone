#!/usr/bin/python3
"""defines class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class REview - inherits BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

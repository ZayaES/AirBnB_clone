#!/usr/bin/python3
"""User class inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """the user class, describes a user of the service"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

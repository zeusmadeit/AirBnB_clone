#!/usr/bin/python3
"""
Write a class User that inherits from BaseModel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """ The User class defines all attributes
        and methods for managing a User.  
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
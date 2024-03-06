#!/usr/bin/python3
"""
Write a class Review that inherits from BaseModel
"""
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
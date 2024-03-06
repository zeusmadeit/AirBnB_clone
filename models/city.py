#!/usr/bin/python3
"""
Write a class City that inherits from BaseModel
"""
from models.base_model import BaseModel

class City(BaseModel):
    name = ""
    state_id = ""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
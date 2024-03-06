#!/usr/bin/python3
"""
Write a class State that inherits from BaseModel
"""
from models.base_model import BaseModel

class State(BaseModel):
    name = ""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
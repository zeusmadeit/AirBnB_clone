#!/usr/bin/python3
""" __init__ file that identifies this folder as a package to the python interpreter"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
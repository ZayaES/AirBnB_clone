#!/usr/bin/python3
"""init module for making a folder a python package
and for defining certain operations"""
from models.engine.file_storage import FileStorage

print("preuse")
storage = FileStorage()
storage.reload()
print("post_use")

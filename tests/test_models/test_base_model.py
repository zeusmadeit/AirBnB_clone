#!/usr/bin/python3
"""test file for the models/base_model module"""
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
import unittest

class TestBaseModel(unittest.TestCase):
    def test_isinstance(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
    
    def test_ID_is_unique(self):
        bm = BaseModel()
        cm = BaseModel()
        dm = BaseModel()
        self.assertTrue(bm.id != cm.id)
        self.assertTrue(bm.id != dm.id)
        self.assertTrue(cm.id != dm.id)

    def test_ID_is_string(self):
        bm = BaseModel()
        self.assertTrue(isinstance(bm.id, str))
    
    def test_save(self):
        bm = BaseModel()
        temp = bm.updated_at
        bm.save()
        self.assertNotEqual(temp, bm.updated_at)
    
    def test_todict(self):
        bm = BaseModel()
        temp = bm.to_dict()
        self.assertIsInstance(temp, dict)
        
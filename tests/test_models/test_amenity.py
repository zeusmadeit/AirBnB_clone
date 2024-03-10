#!/usr/bin/python3
"""
Write a unitetest for the amenity model
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """
    def test_amenity_inherits_from_basemodel(self):
        """
        Test if Amenity class inherits from BaseModel.
        """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_amenity_attributes(self):
        """
        Test if the Amenity class' attributes are properly initialized.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_initialization_with_args(self):
        """
        Test if Amenity class can be initialized with arguments
        and attributes are set accordingly.
        """
        amenity = Amenity(name="Any_Amenity")
        self.assertEqual(amenity.name, "Any_Amenity")

if __name__ == '__main__':
    unittest.main()

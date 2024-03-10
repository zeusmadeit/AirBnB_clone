#!/usr/bin/python3
"""
Write a unitetest for the city model
"""
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """
    def test_city_inherits_from_base_model(self):
        """
        Test if City class inherits from BaseModel.
        """
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

    def test_city_attributes(self):
        """
        Test if attributes of the City class are properly initialized.
        """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_city_initialization_with_args(self):
        """
        Test if City class can be initialized with arguments
        and attributes are set accordingly.
        """
        city = City(name="New York", state_id="NY")
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, "NY")

if __name__ == '__main__':
    unittest.main()

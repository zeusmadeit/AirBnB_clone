#!/usr/bin/python3
"""
Write a unitetest for the place model
"""
import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """
    def test_place_inherits_from_basemodel(self):
        """
        Test if Place class inherits from BaseModel.
        """
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

    def test_place_attributes(self):
        """
        Test if attributes of the Place class are properly initialized.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_initialization_with_args(self):
        """
        Test if Place class can be initialized with arguments
        and attributes are set accordingly.
        """
        place = Place(city_id="12", user_id="34", name="Test Place", description="Description", number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=100, latitude=12.345, longitude=67.890, amenity_ids=[1, 2, 3])
        self.assertEqual(place.city_id, "12")
        self.assertEqual(place.user_id, "34")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "Description")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 12.345)
        self.assertEqual(place.longitude, 67.890)
        self.assertEqual(place.amenity_ids, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

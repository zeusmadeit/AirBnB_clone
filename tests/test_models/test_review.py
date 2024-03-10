#!/usr/bin/python3
"""
Write a unitetest for the review model
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """
    def test_review_inherits_from_base_model(self):
        """
        Test if Review class inherits from BaseModel.
        """
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

    def test_review_attributes(self):
        """
        Test if attributes of the Review class are properly initialized.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_initialization_with_args(self):
        """
        Test if Review class can be initialized with arguments
        and attributes are set accordingly.
        """
        review = Review(place_id="11", user_id="22", text="Test Review")
        self.assertEqual(review.place_id, "11")
        self.assertEqual(review.user_id, "22")
        self.assertEqual(review.text, "Test Review")

    def test_review_attribute_types(self):
        """
        Test if attributes of the Review class are of the correct types.
        """
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

if __name__ == '__main__':
    unittest.main()

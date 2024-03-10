#!/usr/bin/python3
"""
Write a unitetest for the user model
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """
    def test_user_instance(self):
        """
        Test if User instance is created correctly
        and has required attributes.
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_attributes(self):
        """
        Test if User attributes are initialized and can be accessed.
        """
        user = User()
        user.email = "testing@example.com"
        user.password = "password123"
        user.first_name = "Wesam"
        user.last_name = "Eldeeb"

        self.assertEqual(user.email, "testing@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "Wesam")
        self.assertEqual(user.last_name, "Eldeeb")
    
    def test_user_to_dict(self):
        """
        Test if User can be converted to a dictionary correctly.
        """
        user = User()
        user_data = user.to_dict()

        self.assertTrue(isinstance(user_data, dict))
        self.assertEqual(user_data['__class__'], 'User')
        self.assertTrue('id' in user_data)
        self.assertTrue('created_at' in user_data)
        self.assertTrue('updated_at' in user_data)
        self.assertTrue('email' in user_data)
        self.assertTrue('password' in user_data)
        self.assertTrue('first_name' in user_data)
        self.assertTrue('last_name' in user_data)

    def test_user_str_representation(self):
        """
        Test if the string representation of User object is correct.
        """
        user = User()
        user.email = "testing@example.com"
        user.password = "password123"
        user.first_name = "Wesam"
        user.last_name = "Eldeeb"

        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

if __name__ == '__main__':
    unittest.main()
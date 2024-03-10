#!/usr/bin/python3
"""
Write a unitetest for the state model
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """
    def test_state_instance(self):
        """
        Test if State instance is created correctly
        and has required attributes.
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_state_attributes(self):
        """
        Test if State attributes are initialized and accessible.
        """
        state = State()
        state.name = "New York"

        self.assertEqual(state.name, "New York")

    def test_state_to_dict(self):
        """
        Test if State can be converted to a dictionary correctly.
        """
        state = State()
        state.name = "New York"
        state_data = state.to_dict()

        self.assertTrue(isinstance(state_data, dict))
        self.assertEqual(state_data['__class__'], 'State')
        self.assertTrue('id' in state_data)
        self.assertTrue('created_at' in state_data)
        self.assertTrue('updated_at' in state_data)
        self.assertTrue('name' in state_data)

    def test_state_str_representation(self):
        """
        Test if the string representation of State object is correct.
        """
        state = State()
        state.name = "New York"

        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

if __name__ == '__main__':
    unittest.main()

# test_helpertutor.py
"""
Tests for HelperTutor module.
"""

import unittest
from helpertutor import HelperTutor

class TestHelperTutor(unittest.TestCase):
    """Test cases for HelperTutor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HelperTutor()
        self.assertIsInstance(instance, HelperTutor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HelperTutor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_decentrocore.py
"""
Tests for DecentroCore module.
"""

import unittest
from decentrocore import DecentroCore

class TestDecentroCore(unittest.TestCase):
    """Test cases for DecentroCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentroCore()
        self.assertIsInstance(instance, DecentroCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentroCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

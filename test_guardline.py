# test_guardline.py
"""
Tests for GuardLine module.
"""

import unittest
from guardline import GuardLine

class TestGuardLine(unittest.TestCase):
    """Test cases for GuardLine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GuardLine()
        self.assertIsInstance(instance, GuardLine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GuardLine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

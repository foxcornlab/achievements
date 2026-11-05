"""Tests for tools module."""
import unittest
from tools import calculate_stats

class TestTools(unittest.TestCase):
    def test_calculate_stats(self):
        result = calculate_stats([10, 20, 30])
        self.assertEqual(result["count"], 3)
        self.assertEqual(result["mean"], 20.0)
        self.assertEqual(result["total"], 60.0)

    def test_empty_stats(self):
        result = calculate_stats([])
        self.assertEqual(result["count"], 0)

if __name__ == "__main__":
    unittest.main()

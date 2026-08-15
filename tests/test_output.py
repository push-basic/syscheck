import unittest
from pathlib import Path

from src.output import system_output

class TestSystemOutput(unittest.TestCase):

    def test_empty_path(self):
        with self.assertRaises(ValueError):
            system_output(Path())
    
    def test_none_path(self):
        with self.assertRaises(ValueError):
            system_output(None)


if __name__ == "__main__":
    unittest.main()
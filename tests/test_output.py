import unittest
from pathlib import Path

from src.output import system_output

class TestSystemOutput(unittest.TestCase):

    def test_empty_path(self):
        result = system_output(Path())
        self.assertEqual(result, "Error: invalid system path")

    def test_none_path(self):
        result = system_output(None)
        self.assertEqual(result, "Error: invalid system path")


if __name__ == "__main__":
    unittest.main()
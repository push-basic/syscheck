import unittest

from src.output import system_output

class TestSystemOutput(unittest.TestCase):

    def test_empty_path(self):
        with self.assertRaises(ValueError):
            system_output("")
    
    def test_none_path(self):
        with self.assertRaises(ValueError):
            system_output(None)


if __name__ == "__main__":
    unittest.main()
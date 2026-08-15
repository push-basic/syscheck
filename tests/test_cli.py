import unittest
import sys
from pathlib import Path
from io import StringIO
from unittest.mock import patch

from src.cli import main

class TestMain(unittest.TestCase):

    def test_main(self):
        with patch("src.cli.system_output") as mock_system_output:
            mock_system_output.return_value = "healthy"

            with patch.object(sys, "argv", ["cli"]):
                with patch.object(sys, "stdout", new=StringIO()) as stdout:
                    main()

            mock_system_output.assert_called_once_with(Path("/"))
            self.assertEqual(stdout.getvalue(), "healthy\n")



if __name__ == "__main__":
    unittest.main()
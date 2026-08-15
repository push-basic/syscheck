import unittest
from unittest.mock import patch

from socket import gaierror
from pathlib import Path

from src.checks import (
    check_system_health, 
    check_internet, 
    check_dns
)

class TestCheckSystemHealth(unittest.TestCase):

    def test_empty_path(self):
        result = check_system_health(Path())
        self.assertEqual(result, "Error: invalid system path")

    def test_none_path(self):
        result = check_system_health(None)
        self.assertEqual(result, "Error: invalid system path")


class TestCheckInternet(unittest.TestCase):

    @patch("system_health.socket.create_connection")
    def test_internet_reachable(self, mock_create_connection):
        result = check_internet()

        self.assertTrue(result)
        mock_create_connection.assert_called_once_with(
            ("8.8.8.8, 53"),
            timeout=3
        )

    @patch("system_health.socket.create_connection")
    def test_internet_unreachable(self, mock_create_connection):
        mock_create_connection.side_effect = OSError

        result = check_internet()

        self.assertFalse(result)


class TestCheckDns(unittest.TestCase):

    @patch("system_health.socket.gethostbyname")
    def test_dns_working(self, mock_gethostbyname):
        result = check_dns()

        self.assertTrue(result)
        mock_gethostbyname.assert_called_once_with(
            ("https://google.com")
        )

    @patch("system_health.socket.gethostbyname")
    def test_dns_down(self, mock_gethostbyname):
        mock_gethostbyname.side_effect = gaierror
    
        result = check_dns()

        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()
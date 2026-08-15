import unittest
import socket
from unittest.mock import patch

from syscheck.checks import (
    check_system_health, 
    check_internet, 
    check_dns
)

class TestCheckSystemHealth(unittest.TestCase):

    def test_empty_path(self):
        with self.assertRaises(ValueError):
            check_system_health("")

    def test_none_path(self):
        with self.assertRaises(ValueError):
            check_system_health(None)


class TestCheckInternet(unittest.TestCase):

    def test_check_internet_returns_true(self):
        with patch("syscheck.checks.socket.create_connection") as mock_create_connection:
            mock_create_connection.return_value.__enter__.return_value = None

            self.assertTrue(check_internet())



class TestCheckDns(unittest.TestCase):

    def test_check_dns_returns_true_when_resolved(self):
        with patch("syscheck.checks.socket.gethostbyname") as mock_gethostbyname:
            mock_gethostbyname.return_value = "142.250.74.14"

            result = check_dns()

            self.assertTrue(result)
            mock_gethostbyname.assert_called_once_with("google.com")

    def test_check_dns_returns_false_when_unresolved(self):
        with patch("syscheck.checks.socket.gethostbyname") as mock_gethostbyname:
            mock_gethostbyname.side_effect = socket.gaierror

            result = check_dns()

            self.assertFalse(result)
            mock_gethostbyname.assert_called_once_with("google.com")




if __name__ == "__main__":
    unittest.main()
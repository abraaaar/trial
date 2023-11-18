"""
This module contains a login function and its unit tests.
"""

def login(username, password):
    """
    This function checks if the username and password match 'admin' and 'password'.

    Args:
        username (str): The username.
        password (str): The password.

    Returns:
        bool: True if the username and password match, False otherwise.
    """
    if username == 'admin' and password == 'password':
        return True
    return False

import unittest

class TestLogin(unittest.TestCase):
    """
    This class contains unit tests for the login function.
    """

    def test_login(self):
        """
        This method tests the login function with correct and incorrect credentials.
        """
        self.assertTrue(login('admin', 'password'))
        self.assertFalse(login('user', 'pass'))

if __name__ == '__main__':
    unittest.main()

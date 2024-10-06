import unittest
from unittest.mock import patch
from main import fetch_data  # Make sure to import your function
import requests

class TestFetchData(unittest.TestCase):

    @patch('main.requests.get')
    def test_fetch_data_success(self, mock_get):
        # Arrange: Set up the mock to return a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'login': 'octocat',
            'bio': 'A octocat',
            'public_repos': 5
        }

        # Act: Call the function with a test URL
        url = "https://api.github.com/users/octocat"
        result = fetch_data(url)

        # Assert: Check the results
        self.assertIsNotNone(result)
        self.assertEqual(result['login'], 'octocat')
        self.assertEqual(result['bio'], 'A octocat')
        self.assertEqual(result['public_repos'], 5)

    @patch('main.requests.get')
    def test_fetch_data_failure(self, mock_get):
        # Arrange: Set up the mock to raise an exception
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        # Act: Call the function with a test URL
        url = "https://api.github.com/users/octocat"
        result = fetch_data(url)

        # Assert: Check that the result is None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

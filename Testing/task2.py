from phonebook import first_name_search
import unittest
from unittest.mock import patch, mock_open


class TestFirstNameSearch(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='[{"first_name": "Petro"}, {"first_name": "Petro2"}]')
    def test_search_existing_name(self, mock_file):
        result = first_name_search("Petro", "test_file.json")
        self.assertEqual(result, [{"first_name": "Petro"}])

    @patch("builtins.open", new_callable=mock_open, read_data='[{"first_name": "Petro"}, {"first_name": "Petro2"}]')
    def test_search_non_existing_name(self, mock_file):
        result = first_name_search("Petro3", "test_file.json")
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open):
        with self.assertRaises(FileNotFoundError):
            first_name_search("John", "non_existing_file.json")

if __name__ == "__main__":
    unittest.main()
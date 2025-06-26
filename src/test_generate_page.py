import unittest
from generate_page import extract_title

class TestGenerator(unittest.TestCase):
    def test_extract_title(self):
        title = "# Header"
        result = extract_title(title)
        self.assertEqual(result, "Header")
    
    def test_multiple_lines(self):
        lines = """
This is the first line
# This is the Title
This is the last line
"""
        result = extract_title(lines)
        self.assertEqual(result, "This is the Title")

    def test_hash_at_end(self):
        title = "# Heading ends with #"
        result = extract_title(title)
        self.assertEqual(result, "Heading ends with #")

    def test_no_heading(self):
        title = "This title has no heading"
        
        with self.assertRaises(Exception):
            extract_title(title)

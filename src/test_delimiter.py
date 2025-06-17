from typing import assert_type
import unittest
from delimiter import *

class TestDelimiter(unittest.TestCase):
    def test_nodes_delimiter(self):
        input_node = TextNode("This is text with **bold** in the middle", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        
        for node in result:
            print(f"TEXT: {node.text} TYPE: {node.text_type}")
    
    def test_no_delimiter(self):
        input_node = TextNode("This is just plain text", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)
        
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], TextNode)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[0].text, "This is just plain text")  

    def test_missing_delimiter(self):
        input_node = TextNode("Opps I _may have forgotten a delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([input_node], "_", TextType.ITALIC)
    
    def test_multiple_delimiters(self):
        input_node = TextNode("We're in **Hell** but fuck **God** anyways", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "**", TextType.BOLD)

        for node in result:
            print(f"TEXT: {node.text} TYPE: {node.text_type}")

    def test_delimiters_at_start(self):
        input_node = TextNode("_Bulbasaur_ is the best starter", TextType.TEXT)
        result = split_nodes_delimiter([input_node], "_", TextType.ITALIC)

        for node in result:
            print(f"TEXT: {node.text} TYPE: {node.text_type}")
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to wikipedia](https://en.wikipedia.org)"
        )
        self.assertListEqual([("to wikipedia", "https://en.wikipedia.org")], matches)
    
    def test_extract_markdown_empty(self):
        sample = extract_markdown_images("this is a string with no images or links")
        sample2 = extract_markdown_links("this is a string with no images or links")
        self.assertEqual([], sample)
        self.assertEqual([], sample2)

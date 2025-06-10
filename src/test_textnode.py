import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Coding is hard when you're dyslexic", TextType.ITALIC)
        node2 = TextNode("Coding is hard when your dyslexic", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This game is addicting", TextType.TEXT, "https://orteil.dashnet.org/cookieclicker")
        node2 = TextNode("This game is addicting", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
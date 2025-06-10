import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag="a", props={"href": "https://boot.dev", "target": "_blank"})
        print(node.props_to_html())
    
    def test_value(self):
        node = HTMLNode(value="Vikk is my goddess")
        print(f"NODE DATA: {node.tag}, {node.value}, {node.children}, {node.props}")
    
    def test_repr(self):
        node = HTMLNode(tag="p", value="I love Vikk", props={"href": "https://Vikkphoria.ar", "target": "_blank"})
        print(node)
    
    def test_empty_props(self):
        node = HTMLNode(tag="a", value="Thanks for everything, love")
        print(node.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hail Satan")
        self.assertEqual(node.to_html(), "<p>Hail Satan</p>")
    
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "X? No we have twitter at home.", {"href": "https://bsky.app"})
        self.assertEqual(node.to_html(), '<a href="https://bsky.app">X? No we have twitter at home.</a>')
    
    def test_leaf_missing_tag(self):
        node = LeafNode(None, "Tag you're it!")
        print(node.to_html())

if __name__ == "__main__":
    unittest.main()
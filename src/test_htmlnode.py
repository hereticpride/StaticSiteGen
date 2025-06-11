import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span","child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_empty_list(self):
        parent_node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
from sys import exception
from textnode import TextType, TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
        if self.children == None:
            self.children = []
        if self.props == None:
            self.props = {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        result = ""
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        return result
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("leaf node has no value")
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(tag, value, None, props)

    def to_html(self):
        props_str = ""

        if self.value == None:
            raise ValueError("leaf node has no value")
        elif self.tag == None:
            return self.value
        else:
            #I already handled this in props_to_html, this is completely redundant
            #for key, val in self.props.items(): 
                    #props_str += f' {key}="{val}"'
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        def __repr__(self):
            return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children == None:
            raise ValueError("ParentNode children property cannot be None")
        
        self.tag = tag
        self.children = children
        self.props = props
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode had no tag property")
        elif self.children == None:
            raise ValueError("ParentNode has no children")
        elif not self.children:
            raise ValueError("Children is an empty list. ParentNode must have atleast (1) child")
        else:
            result = ""
            for child in self.children:
                result += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
        
        def __repr__(self):
            return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href" : text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text})
    else:
        raise Exception("TextNode must have valid TextType")
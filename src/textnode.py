from enum import Enum

class TextType(Enum):
    normal_text = "normal"
    bold_text = "bold"
    italic_text = "italic"
    code_text = "code"
    link_text = "link"
    image_text = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if isinstance(other, TextNode):
            if (self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url):
                return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

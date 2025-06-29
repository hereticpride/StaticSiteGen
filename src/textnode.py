from enum import Enum

class TextType(Enum):
    TEXT = "TextType.TEXT"
    BOLD = "TextType.BOLD"
    ITALIC = "TextType.ITALIC"
    CODE = "TextType.CODE"
    LINK = "TextType.LINK"
    IMAGE = "TextType.IMAGE"

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

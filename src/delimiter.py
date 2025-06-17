import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        else:
            segments = node.text.split(delimiter)
            if len(segments) % 2 == 0:
                raise ValueError("Invalid Markdown syntax: missing closing delimiter")
            
            for idx, seg in enumerate(segments):
                if idx % 2 == 0:
                    new_node = TextNode(seg, TextType.TEXT)
                
                else:
                    new_node = TextNode(seg, text_type)
                node_list.append(new_node)
    return node_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
                
                
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

text2 = "This is text with a link [to wikipedia](https://en.wikipedia.org)"
print(extract_markdown_links(text2))

sample = "Here is ![alt1](url1.png) and [anchor](url2.com)"
print(extract_markdown_images(sample))
print(extract_markdown_links(sample))

sample2 = "Here is alt1 url1.png and anchor url2.com"
print(extract_markdown_images(sample2))
print(extract_markdown_links(sample2))

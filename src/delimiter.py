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

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        else:
            links = extract_markdown_images(node.text)
            remaining_text = node.text
            for link in links:
                segments = remaining_text.split(f"![{link[0]}]({link[1]})", 1)
                remaining_text = segments[1]
                if segments[0] != "":
                    seg = TextNode(segments[0], TextType.TEXT)
                    node_list.append(seg)
                link_node = TextNode(link[0], TextType.IMAGE, link[1])
                node_list.append(link_node)
            if remaining_text != "":
                rt_string = TextNode(remaining_text, TextType.TEXT)
                node_list.append(rt_string)
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        else:
            links = extract_markdown_links(node.text)
            remaining_text = node.text
            for link in links:
                segments = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
                remaining_text = segments[1]
                if segments[0] != "":
                    seg = TextNode(segments[0], TextType.TEXT)
                    node_list.append(seg)
                link_node = TextNode(link[0], TextType.LINK, link[1])
                node_list.append(link_node)
            if remaining_text != "":
                rt_string = TextNode(remaining_text, TextType.TEXT)
                node_list.append(rt_string)
    return node_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


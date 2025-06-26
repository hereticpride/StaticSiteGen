from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from inline_markdown import text_to_textnode
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading" #Headings start with 1-6 # characters, followed by a space and then the heading text.
    CODE = "code" #Code blocks must start with 3 backticks and end with 3 backticks
    QUOTE = "quote" #Every line in a quote block must start with a > character.
    UNORDERED_LIST = "unordered list" #Every line in an unordered list block must start with a - character, followed by a space.
    ORDERED_LIST = "ordered list" #a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.


    
def block_to_block_type(markdown):
    #takes markdown text and returns the blocktype
    if (markdown.startswith("# ") or
        markdown.startswith("## ") or
        markdown.startswith("### ") or 
        markdown.startswith("#### ") or
        markdown.startswith("##### ") or
        markdown.startswith("###### ")):
        return BlockType.HEADING
    elif markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    elif all(item.startswith('>') for item in markdown.split("\n")):
        return BlockType.QUOTE
    elif all(item.startswith('- ') for item in markdown.split("\n")):
        return BlockType.UNORDERED_LIST
    else:
        #this boolean is redundant because I refactured this entire block but leaving it in as a reminder that I am better than my instructors
        is_ordered_list = True
        x = 1
        lines = markdown.split("\n")

        if not lines:
            is_ordered_list = False
            return BlockType.PARAGRAPH
        
        for line in lines:
            expected_prefix = f"{x}. "
            if not line.startswith(expected_prefix):
                is_ordered_list = False
                return BlockType.PARAGRAPH

            x += 1
        
        return BlockType.ORDERED_LIST
    
    
    

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            result.append(stripped_block)
    return result

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes_list = []
    for block in blocks:
        segment = block_to_block_type(block)
        #based on block type create new HTMLNode
        if segment == BlockType.PARAGRAPH:
            node = text_to_html_children("p", block)
            nodes_list.append(node)
        elif segment == BlockType.HEADING:
            #need to work on this
            count = count_header(block)
            if count > 0 and block[count:count+1] ==" ":
                text = block[count+1:]
                tag = f"h{count}"
                node = text_to_html_children(tag, text)
            else:
                node = text_to_html_children("p", block)
            nodes_list.append(node)
        elif segment == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = "\n".join([line.lstrip("> ") for line in lines])
            node = text_to_html_children("blockquote", cleaned)
            nodes_list.append(node)     
        elif segment == BlockType.UNORDERED_LIST:
            list_items = []
            for seg in block.split("\n"):
                if seg == "":
                    continue
                node = text_to_html_children("li", seg.removeprefix("- ").strip())
                list_items.append(node)
            node = ParentNode("ul", list_items)
            nodes_list.append(node)
        elif segment == BlockType.ORDERED_LIST:
            list_items = []
            counter = 1
            for seg in block.split("\n"):
                if seg == "":
                    continue
                node = text_to_html_children("li", seg.removeprefix(f"{counter}. ").strip())
                list_items.append(node)
                counter += 1
            node = ParentNode("ol", list_items)
            nodes_list.append(node)
        elif segment == BlockType.CODE:
            code_text = "\n".join(line for line in block.split("\n")[1:-1])
            code_node = LeafNode("code", code_text)
            pre_node = ParentNode("pre", [code_node])
            nodes_list.append(pre_node)
            
    return ParentNode("div", nodes_list)
    
def count_header(header):
    count = 0
    for h in header:
        if h == "#":
            count += 1
        else:
            break
    return count

def text_to_html_children(tag, text):
    text_node = text_to_textnode(text)
    children = [text_node_to_html_node(tex) for tex in text_node]
    return ParentNode(tag, children)
    
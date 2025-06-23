from enum import Enum

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

text = "this is a paragraph"
c = "```this is code```"
h = "### this is a heading"
test1 = block_to_block_type(text)
test2 = block_to_block_type(c)
test3 = block_to_block_type(h)

print(test1)
print(test2)
print(test3)
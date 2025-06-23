import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type


class TestMarkdownToHTML(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "I am not a narcissist I actually am just better than you."
        block_type = block_to_block_type(block)
        self.assertIsInstance(block_type, BlockType)

    def test_ordered_list_block_type(self):
        ordered_list = "" \
        "1. for the money" \
        "2. for the show" \
        "3. to get ready" \
        "4. to... wait I wasn't ready"

        block = block_to_block_type(ordered_list)
        self.assertEqual(block, BlockType.ORDERED_LIST)
    
    def test_not_ordered_list(self):
        disordered_list = """
1. Learn to code
2. Get a job in IT
3. Make Video Games
???
4. Profit
"""
        block = block_to_block_type(disordered_list)
        self.assertNotEqual(block, BlockType.ORDERED_LIST)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


if __name__ == "__main__":
    unittest.main()
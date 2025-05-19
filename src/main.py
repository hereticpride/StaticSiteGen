from textnode import TextNode, TextType


def main():
    text = TextNode("This is some anchor text", TextType.link_text, "https://www.boot.dev")
    print(text)

main()
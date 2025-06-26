import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    print(lines)
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
        else:
            continue
    raise Exception("Markdown has invalid Header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        source = f.read()
    with open(template_path, "r") as t:
        temp = t.read()
    html_node = markdown_to_html_node(source)
    content = html_node.to_html()
    title = extract_title(source)

    new_title = temp.replace("{{ Title }}", f"{title}")
    new_content = new_title.replace("{{ Content }}", f"{content}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as d:
        d.write(new_content)
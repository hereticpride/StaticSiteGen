import os
import pathlib
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

def generate_page(from_path, template_path, dest_path, basepath):
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
    new_href = new_content.replace('href="/', f'href="{basepath}')
    result = new_href.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as d:
        d.write(result)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)
    
    for file in files:
        content = os.path.join(dir_path_content, file)
        html_file = os.path.splitext(file)[0] + ".html"
        dest = os.path.join(dest_dir_path, html_file)
        if os.path.isfile(content) and content.endswith(".md"):
            generate_page(content, template_path, dest, basepath)
        elif os.path.isdir(content):
            pathlib.Path(dest).mkdir(parents=True, exist_ok=True)
            generate_page_recursive(content, template_path, os.path.join(dest_dir_path, file), basepath)
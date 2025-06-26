from textnode import TextNode, TextType
import os
import shutil
from static_copy import copy_directory
from generate_page import generate_page


static_dir_path = "./static"
public_dir_path = "./public"
content = "./content/index.md"
template = "./template.html"
public = "./public/index.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    
    print("Copying static files to public directory...")
    copy_directory(static_dir_path, public_dir_path)
    generate_page(content, template, public)


main()
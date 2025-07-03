import sys
from textnode import TextNode, TextType
import os
import shutil
from static_copy import copy_directory
from generate_page import generate_page_recursive


static_dir_path = "./static"
public_dir_path = "./docs"
content = "./content"
template = "./template.html"
public = "./docs/index.html"

if len(sys.argv) > 1:
    basepath = sys.argv[1]

else:
    basepath = "/"

if not basepath.startswith("/"):
    basepath = "/" + basepath
if not basepath.endswith("/"):
    basepath = basepath + "/"

def main():
    print("Deleting public directory...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    
    print("Copying static files to public directory...")
    copy_directory(static_dir_path, public_dir_path)
    generate_page_recursive(content, template, public_dir_path, basepath)
    


main()
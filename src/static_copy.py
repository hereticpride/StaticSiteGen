import os
import shutil

def copy_directory(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for dir in os.listdir(source):
        origin_path = os.path.join(source, dir)
        new_path = os.path.join(dest, dir)
        print(f" * {origin_path} -> {new_path}")
        if os.path.isfile(origin_path):
            shutil.copy(origin_path, new_path)
        else:
            copy_directory(origin_path, new_path)
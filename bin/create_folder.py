import os

def create_dir(parent_dir, new_dir_name):
    # Check if path already exists
    new_path = os.path.join(parent_dir, new_dir_name)
    if os.path.isdir(new_path):
        return new_path

    # Create dir with images
    try: 
        os.mkdir(new_path)
        return new_path
    except OSError as error:
        print(new_path, error)
        return False

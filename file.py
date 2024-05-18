import os

def print_directory_structure(root_dir, prefix=''):
    """
    Prints the directory structure of the given root directory.
    
    Args:
        root_dir (str): The root directory to start printing the structure from.
        prefix (str): The prefix for each directory/file, used for indentation.
    """
    try:
        contents = os.listdir(root_dir)
        contents.sort()
        for index, name in enumerate(contents):
            path = os.path.join(root_dir, name)
            connector = '└── ' if index == len(contents) - 1 else '├── '
            print(f"{prefix}{connector}{name}")
            if os.path.isdir(path):
                new_prefix = '    ' if index == len(contents) - 1 else '│   '
                print_directory_structure(path, prefix + new_prefix)
    except PermissionError:
        print(f"{prefix}[Permission Denied]")

# Define the root directory of your ROS 2 workspace
root_directory = os.path.abspath(os.curdir)

# Print the directory structure
print(f"Directory structure for: {root_directory}\n")
print_directory_structure(root_directory)

import os

def read_folder_structure(base_path, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(base_path):
            level = root.replace(base_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(subindent, file))
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_content:
                    content = file_content.read()
                    f.write('{}Content of {}:\n{}\n\n'.format(subindent, file, content))

# Define the base path for the project and the output file
base_path = 'D:\\KassowRobotProject'
output_file = 'D:\\folder_structure.txt'

# Read the folder structure and write to the output file
read_folder_structure(base_path, output_file)

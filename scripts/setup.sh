import os

# Define the base path for your project
base_path = 'D:\\KassowRobotProject'
scripts_path = os.path.join(base_path, 'scripts')

# Ensure the scripts directory exists
os.makedirs(scripts_path, exist_ok=True)

# Define the content of the setup.sh file
setup_sh_content = '''#!/bin/bash

# Setup script
'''

# Create the setup.sh file with the specified content
setup_sh_path = os.path.join(scripts_path, 'setup.sh')
with open(setup_sh_path, 'w') as f:
    f.write(setup_sh_content)

# Make the script executable
os.chmod(setup_sh_path, 0o755)

print(f"setup.sh created at: {setup_sh_path}")

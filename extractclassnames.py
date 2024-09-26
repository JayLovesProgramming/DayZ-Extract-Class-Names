import os
import re

# Directory where the folders containing config.cpp files are located
root_directory = os.getcwd()

# Regex pattern to match class names (e.g., class HMB_Karambit_Black)
class_pattern = re.compile(r'class\s+(HMB_\w+)')

# List to store all found class names
class_names = []

def find_classes_in_config(file_path):
    """Reads a config.cpp file and extracts class names that start with HMB_."""
    with open(file_path, 'r') as file:
        content = file.read()
        matches = class_pattern.findall(content)
        return matches

def scan_directory(directory):
    """Recursively scans the directory for config.cpp files and extracts class names."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'config.cpp':
                file_path = os.path.join(root, file)
                found_classes = find_classes_in_config(file_path)
                class_names.extend(found_classes)

def main():
    scan_directory(root_directory)
    # Write all class names to a text file
    with open('class_names.txt', 'w') as output_file:
        for class_name in class_names:
            output_file.write(f"{class_name}\n")
    print(f"Found {len(class_names)} class names starting with 'HMB_'. Saved to class_names.txt.")

if __name__ == "__main__":
    main()

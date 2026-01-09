# utils.py

import os
import subprocess
import json

def get_directory_path():
    """
    Get the absolute path of the current directory.

    Returns:
        str: The absolute path of the current directory.
    """
    return os.path.dirname(os.path.abspath(__file__))

def get_parent_directory_path():
    """
    Get the absolute path of the parent directory of the current directory.

    Returns:
        str: The absolute path of the parent directory.
    """
    return os.path.dirname(get_directory_path())

def get_terraform_version():
    """
    Get the Terraform version installed on the system.

    Returns:
        str: The Terraform version.
    """
    try:
        output = subprocess.check_output(['terraform', '--version']).decode('utf-8')
        return output.strip().split(' ')[-1]
    except subprocess.CalledProcessError:
        return None

def load_json_file(file_path):
    """
    Load a JSON file into a Python dictionary.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
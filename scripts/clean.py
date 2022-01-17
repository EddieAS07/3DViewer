"""
A script that automates cleaning the project after CMake has run.
"""

import os
from modules import project_utils as utils
import shutil

def clean_project():
    """
    Cleans project generated through CMake.
    """
    
    project_path = utils.get_base_directory_with_folder(os.getcwd(), ".git")

    # Build directories of project
    generated_directories = [
        project_path / "build",
        project_path / "bin",
        project_path / "lib",
        project_path / "include",
    ]

    for directory in generated_directories:
        try:
            shutil.rmtree(directory)
        except OSError as exception:
            print(f"Could not remove directory {directory}:\n{exception}")

def main():
    """
    Starting point of program.
    """

    clean_project()

if __name__ == "__main__":
    main()

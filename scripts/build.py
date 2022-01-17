"""
A script that automates project building with CMake.
"""

import os
import sys
from modules import project_utils as utils

def build_project():
    """
    Builds the project with CMake.
    Returns exit status of program.
    """

    try:
        # Get base project directory
        project_path = utils.get_base_directory_with_folder(os.getcwd(), ".git") 
    except utils.PathNotFoundError:
        print("Cannot find project directory; exiting program")

        return 1
    
    # Build and source directories of project 
    build_directory = project_path / "build"
    source_directory = project_path
    
    # Command to create build system
    cmake_command = rf"cmake -B {str(build_directory)} -S {str(source_directory)}"
    print(cmake_command)
    exit_status = utils.run_shell_command(cmake_command)
    
    if(exit_status != 0):
        return 1

    # Command to build created files into binaries
    build_command = f"cmake --build {str(build_directory)}"
    run_shell_command(cmake_command)

    if(exit_status != 0):
        return 1

    return 0

def main():
    """
    Starting point of program.
    """

    exit_status = build_project()
    if(exit_status != 0):
        sys.exit(exit_status)

if __name__ == "__main__":
    main()

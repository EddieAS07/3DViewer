"""
A script that defines functions and constants 
to help with project building and cleaning.
"""

import os
from pathlib import Path
import shlex
import subprocess

class PathNotFoundError(Exception):
    """
    Exception for when a path cannot be found.
    """

    pass

def go_up_directory(current_path, levels):
    """
    Goes up level number of directories.

    current_path: Current path to operate on.
    levels: How many levels to go up.

    Returns new path.
    """

    new_path = current_path 

    for i in range(levels):
        # Move to parent of directory
        new_path = new_path.parent

    return new_path

def get_base_directory_with_folder(current_path, folder):
    """
    Gets the base directory from current_path where folder is located.
    i.e. Look for where the .git folder is at inside a project.

    current_path: Path object or string where the user currently is.

    Returns a Path object.
    Raises PathNotFoundError if current_path is not inside a directory
    with folder.
    """

    # If string is passed, encapsulate it within a Path object
    if isinstance(current_path, str):
        current_path = Path(current_path)

    # Go up more directories while path does not have folder 
    while not (current_path / folder).is_dir():
        current_path = go_up_directory(current_path, 1)
        
        # If path is the root directory, raise exception 
        if current_path.parent == current_path:
            exception_status = f"Current directory is not within a project that has the folder {folder}"

            raise PathNotFoundError(exception_status) 
    
    return current_path

def run_shell_command(command, return_output = False):
    """
    Runs command as a subprocess inside the current shell.
    command: Command to run.

    Returns the exit status of command.
    """

    # Divide command into list
    argument_list = shlex.split(command, posix=False)
    print(argument_list)
    
    pipe = subprocess.Popen(argument_list)

    # Wait until process is done
    pipe.wait()

    # Return output of command
    if return_output:
       return pipe.returncode, pipe.output

    return pipe.returncode
    

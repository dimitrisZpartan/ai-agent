import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)

    if not os.path.commonpath(
        [os.path.abspath(working_directory), os.path.abspath(full_path)]
    ) == os.path.abspath(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found.'

    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python3", file_path, *args],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.path.abspath(working_directory),
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    if result.returncode != 0:
        return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nProcess exited with code {result.returncode}"

    if not result.stdout and not result.stderr:
        return "No output produced"

    return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"

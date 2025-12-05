import os


def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)

    if not os.path.commonpath(
        [os.path.abspath(working_directory), os.path.abspath(full_path)]
    ) == os.path.abspath(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    dir = os.path.dirname(full_path)
    if dir and not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

    with open(full_path, "w") as f:
        f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

import os


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)

        if not os.path.commonpath(
            [os.path.abspath(working_directory), os.path.abspath(full_path)]
        ) == os.path.abspath(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, "r") as f:
            file_content_string = f.read()

        if len(file_content_string) > 10000:
            file_content_string = f'{file_content_string[:10001]}\n[...File "{file_path}" truncated at 10000 characters].'

    except Exception as e:
        print(f"Error: {e}")

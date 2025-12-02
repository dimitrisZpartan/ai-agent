import os


def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)

        if not os.path.commonpath(
            [os.path.abspath(working_directory), os.path.abspath(full_path)]
        ) == os.path.abspath(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        dir_content = list(os.listdir(full_path))

        file_info = []
        for content in dir_content:
            file_path = os.path.join(full_path, content)
            file_info.append(
                f"- {content}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
            )

        return "\n".join(file_info)

    except Exception as e:
        return f"Error: {e}"

def truncate(file_path):
    with open(file_path, "r") as f:
        if len(f.read()) < 10000:
            return f.read()
        return (
            f'{f.read(10000)}\n[...File "{file_path}" truncated at 10000 characters].'
        )

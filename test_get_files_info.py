from functions.get_files_info import get_files_info

test_cases = [
    (
        "calculator",
        ".",
    ),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]


def main():
    for case in test_cases:
        info = get_files_info(case[0], case[1]).split("\n")
        if case[1] == ".":
            print("Result for current directory")
            print(f"    {'\n    '.join(info)}\n")
        else:
            print(f"Result for '{case[1]}' directory")
            print(f"    {'\n    '.join(info)}\n")


if __name__ == "__main__":
    main()

from functions.get_file_content import get_file_content

test_cases = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]


def main():
    for case in test_cases:
        content = get_file_content(case[0], case[1])
        print(f"Result for '{case[1]}'")
        print(content)


if __name__ == "__main__":
    main()

from functions.run_python_file import run_python_file

test_cases = [
    ("calculator", "main.py"),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py"),
    ("calculator", "lorem.txt"),
]


for case in test_cases:
    if len(case) == 3:
        result = run_python_file(case[0], case[1], case[2])
    result = run_python_file(case[0], case[1])

    print(f"Result for {case[1]}:")
    print(result)
    print("-" * 40)

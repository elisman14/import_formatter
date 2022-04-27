from pyparsing import line
from py_project_formatter.files_iterator import find_files
from py_project_formatter.imports_formatter import sort_imports


def do_task():
    paths: list[str] = find_files()
    for path in paths:
        with open(path, "r") as f:
            sorted_file: str = sort_imports(f.read())
        with open(path, "w") as f:
            f.write(sorted_file)



from pyparsing import line
from py_project_formatter.files_iterator import find_files
from py_project_formatter.imports_formatter import sort_imports


def do_task():
    paths: list[str] = find_files()
    for path in paths:
        with open(path, 'r+') as opened_file:
            sorted_file: str = sort_imports(opened_file.read())
            opened_file.truncate(0)
            opened_file.write(sorted_file)



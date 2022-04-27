from py_project_formatter.files_iterator import find_files


# def test_files_count():
#     assert len(find_files()) == 10


def test_files_is_py():
    after: list[str] = find_files()
    for name in after:
        assert name.endswith(".py")

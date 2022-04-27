from py_project_formatter.imports_formatter import sort_imports 


def test_sort_imports():
    for i in range(0, 5):
        with open("./tests/sort_imports_testfiles/" + str(i) + ".py", 'r') as before:
            after: str = sort_imports(before.read())
            mustbe: str = open("./tests/sort_imports_testfiles/" + str(i) + " copy.py", 'r')
            msg: str = f"{after=}, {i=}"
            assert after == mustbe.read(), msg
            mustbe.close()

import a
import b
from s import z
from y import x
def test_files_is_py():
    after: list[str] = find_files()
    for name in after:
        assert name.endswith(".py")

from y import x
    
import b
    
    
    
    
import a
    
    
    
from s import z
    
    
    
def test_files_is_py():
    after: list[str] = find_files()
    for name in after:
        assert name.endswith(".py")
        
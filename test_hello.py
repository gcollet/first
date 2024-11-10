"""
    Test hello.py
"""
import pathlib

def test_exist():
    """Test just the existence of the file hello.py"""
    assert pathlib.Path("hello.py").is_file()

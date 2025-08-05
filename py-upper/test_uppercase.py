import pytest
from uppercase import to_uppercase

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("Hello World") == "HELLO WORLD"
    assert to_uppercase("123") == "123"
    assert to_uppercase("") == ""
if __name__ == "__main__":
    pytest.main()
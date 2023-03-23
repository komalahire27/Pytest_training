import pytest

@pytest.fixture
def fixture1():
    return [1, 2, 3]
    #assert fixture1 == [1, 2, 3]
def test_sum(fixture1):
    assert sum(fixture1) == 6

def test_len(fixture1):
    assert len(fixture1) == 3
import pytest

@pytest.fixture
def sample():
    return [1, 2, 3, 4, 5]

def test_sum(sample):
    assert sum(sample) == 15
import pytest

@pytest.mark.xfail

def test_fail():
    assert False

@pytest.mark.skip

def test_skip():
    assert True


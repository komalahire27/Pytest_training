import pytest

@pytest.fixture(scope='module')

def mod_scope():
    list = [1, 2, 3]
    yield list

def test_sum(mod_scope):
    assert sum(mod_scope) == 6

def test_len(mod_scope):
    assert len(mod_scope) == 3
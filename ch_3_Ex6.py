import pytest

@pytest.fixture(scope='module')
def mod_scope():
    return [1, 2, 3]

def test_sum(mod_scope):
    assert sum(mod_scope) == 6

def test_len(mod_scope):
    assert len(mod_scope) == 3
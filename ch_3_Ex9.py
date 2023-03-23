import pytest

@pytest.fixture(scope='module')

def mod_scope():
    list = [1, 2, 3]
    print("Start yield function")
    yield list
    print("End yield function")

def test_len(mod_scope):
    assert len(mod_scope) == 3

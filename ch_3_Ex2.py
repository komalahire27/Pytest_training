import pytest

@pytest.fixture()
def list_fixture():
    return [1, 2, 3, 4, 5]  #fixture returns  number of list

@pytest.fixture()
def dict_fixture():
    return {'name': 'komal', 'age': 23}     #fixture returns  number of person info

@pytest.fixture()
def tuple_fixture():
    return ("A", "B", "C")  #fixture returns tuple of string

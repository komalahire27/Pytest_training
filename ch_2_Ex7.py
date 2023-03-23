import pytest
import tasks
from tasks import Task
def test_count1():
    assert tasks.count() == 0

def test_count():
    tasks.add(Task("T1"))
    assert tasks.count() == 1


import pytest
import tasks
from tasks import Task, TaskStatus
from tasks.exceptions import DuplicateIDError
def test_add():

    task = Task('Duplicate ID', status=TaskStatus.DONE)
    tasks.add(task)
    with pytest.raises(DuplicateIDError):
        tasks.add(task)

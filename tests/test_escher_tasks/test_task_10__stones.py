import pytest
from tasks.escher_tasks.task_10__stones import stones_recursion, stones_queue, stones_dynamic


@pytest.mark.parametrize("f", [stones_recursion, stones_queue, stones_dynamic])
def test_stones(f):
    assert f(17, [1, 3, 4]) == 2
    assert f(17, [1, 3, 4, 6, 9]) == 1
    assert f(99, [1]) == 2

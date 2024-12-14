import pytest
from tasks.escher_tasks.task_9__treasures import (
    treasures, treasures_2, treasures_3)


@pytest.mark.parametrize("func", [treasures, treasures_2, treasures_3])
def test_treasures(func):

    assert func(
        {'golden coin': {'price': 100, 'weight': 50, 'amount': 200},
         'silver coin': {'price': 10, 'weight': 20, 'amount': 1000},
         'ruby': {'price': 1000, 'weight': 200, 'amount': 2}}, 5
    ) == ['golden coin: 92', 'ruby: 2']

    assert func(
        {'golden coin': {'price': 100, 'weight': 50, 'amount': 100},
         'silver coin': {'price': 10, 'weight': 20, 'amount': 100},
         'ruby': {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5
    ) == ['golden coin: 100', 'silver coin: 100', 'ruby: 1']

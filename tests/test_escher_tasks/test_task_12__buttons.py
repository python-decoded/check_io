import pytest
from tasks.escher_tasks.task_12__buttons import buttons, buttons_2


@pytest.mark.parametrize("func", [buttons, buttons_2])
def test_buttons(func):

    assert func('''
001203
023001
100220''') == [8, 4, 4, 1]

    assert func('''
000000
000055
000055''') == [20]

    assert func('''
908070
060504
302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]

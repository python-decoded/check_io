import pytest
from tasks.escher_tasks.task_4__stone_wall import stone_wall_1, stone_wall_2


@pytest.mark.parametrize("func", [stone_wall_1, stone_wall_2])
def test_stone_wall(func):

    assert func('''
##########
####0##0##
00##0###00
''') == 4

    assert func('''
#00#######
#######0##
00######00
''') == 1

    assert func('''
#####
#####
#####
''') == 0

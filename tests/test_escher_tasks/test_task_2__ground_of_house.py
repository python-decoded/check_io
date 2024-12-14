import pytest
from tasks.escher_tasks.task_2__ground_of_house import house, house_2


@pytest.mark.parametrize("function", [house, house_2])
def test_house(function):

    assert function('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24     # up 1, down 4, left 0, right 5

    assert function('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert function('''0000
0000
#000
''') == 1

    assert function('''0000
0000
''') == 0

    assert function('''
0##0
0000
#00#
''') == 12

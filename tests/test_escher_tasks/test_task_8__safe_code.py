import pytest
from tasks.escher_tasks.task_8__safe_code import safe_code


@pytest.mark.parametrize("equation, res", [
    ("-5#*-1=5#", 0),
    ("5#*-1=-5#", 0),
    ("##*##=302#", 5),
    ("19--45=5#", -1),
    ("##--11=11", -1),
    ("#9+3=22", 1),
    ("11*#=##", 2),
    ("#9+3=12", -1),
])
def test_safe_code(equation, res):
    assert safe_code(equation) == res

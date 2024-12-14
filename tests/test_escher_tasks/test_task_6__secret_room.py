import pytest
from tasks.escher_tasks.task_6__secret_room import secret_room, translated


@pytest.mark.parametrize("val, res", [
    (0, "zero"),
    (1, "one"),
    (100, "one hundred"),
    (101, "one hundred one"),
    (119, "one hundred nineteen"),
    (500, "five hundred"),
    (229, "two hundred twenty nine"),
    (109, "one hundred nine"),
    (129, "one hundred twenty nine"),
    (1000, "one thousand")
])
def test_translated(val, res):
    assert translated(val) == res


def test_secret_room():
    assert secret_room(5) == 1  # five, four, one, three, two
    assert secret_room(3) == 2  # one, three, two
    assert secret_room(1000) == 551

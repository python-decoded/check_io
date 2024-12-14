import pytest

from tasks.season_1.sum_numbers import sum_numbers


@pytest.mark.parametrize(["param", "res"], [
    ["hi", 0],
    ['who is 1st here', 0],
    ["my numbers is 2", 2],
    ['This picture is an oil on canvas '
     'painting by Danish artist Anna '
     'Petersen between 1845 and 1910 year', 3755],
    ['5 plus 6 is', 11],
    ['-5 plus 6 is', 1],
    ["", 0],
])
def test_sum_numbers(param, res):
    assert sum_numbers(param) == res

import pytest

from tasks.season_1.acceptable_password import is_acceptable_password


@pytest.mark.parametrize(["data", "is_valid"], [
    ["short", False],
    ['short54', True],
    ['muchlonger', True],
    ['ashort', False],
    ['muchlonger5', True],
    ['sh5', False],
    ['1234567', False],
    ['12345678910', True],
    ['password12345', False],
    ['PASSWORD12345', False],
    ['pass1234word', True]
])
def test_acceptable_password(data, is_valid):
    assert is_acceptable_password(data) == is_valid

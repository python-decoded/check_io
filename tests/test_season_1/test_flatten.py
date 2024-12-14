import pytest

from tasks.season_1.flatten import flat_list, flat_list_while


@pytest.mark.parametrize("func", [flat_list, flat_list_while])
@pytest.mark.parametrize(["data", "res"], [
    [[], []],
    [[1, 2, 3], [1, 2, 3]],
    [[1, [2, 2, 2], 4], [1, 2, 2, 2, 4]],
    [[[[2]], [4, [5, 6, [6], 6, 6, 6], 7]], [2, 4, 5, 6, 6, 6, 6, 6, 7]],
    [[-1, [1, [-2], 1], -1], [-1, 1, -2, 1, -1]]
])
def test_flatten(func, data, res):
    assert func(data) == res

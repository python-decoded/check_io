import pytest

from tasks.season_1.majority import (is_majority, is_majority_count, is_majority_len,
                                     is_majority_sum, is_majority_agg)


@pytest.mark.parametrize("func", [
    is_majority,
    is_majority_count,
    is_majority_len,
    is_majority_sum,
    is_majority_agg
])
@pytest.mark.parametrize(["data", "res"], [
    [[True, True, False, True, False], True],
    [[True, True, False], True],
    [[True, True, False, False], False],
    [[True, True, False, False, False], False],
    [[False], False],
    [[True], True],
    [[], False],
])
def test_majority(func, data, res):
    assert func(data) == res

import pytest

from tasks.season_1.non_unique import checkio, checkio_gen, checkio_list_comp, checkio_filter


@pytest.mark.parametrize("func", [
    checkio, checkio_gen, checkio_list_comp, checkio_filter
])
@pytest.mark.parametrize(["collection", "res"], [
    [[1, 2, 3, 1, 3], [1, 3, 1, 3]],
    [[1, 2, 3, 4, 5], []],
    [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
    [[10, 9, 10, 10, 9, 8], [10, 9, 10, 10, 9]],
])
def test_non_unique(func, collection, res):
    assert func(collection) == res

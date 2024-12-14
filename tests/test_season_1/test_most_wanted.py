import pytest

from tasks.season_1.most_wanted import checkio, checkio_max


@pytest.mark.parametrize("func", [checkio, checkio_max])
@pytest.mark.parametrize(["text", "res"], [
    ["Hello World!", "l"],
    ["How do you do?", "o"],
    ["One", "e"],
    ["Oops!", "o"],
    ["AAaooo!!!!", "a"],
    ["abe", "a"],
    ["a" * 9000 + "b" * 1000, "a"],
    ["oooAAa!!!!", "a"],
])
def test_most_wanted(func, text, res):
    assert func(text) == res

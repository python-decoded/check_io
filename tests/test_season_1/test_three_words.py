import pytest

from tasks.season_1.three_words import checkio, all_words_are_text


@pytest.mark.parametrize(["words", "expected"], [
    ["Hello World hello", True],
    ["He is 123 man", False],
    ["1 2 3 4", False],
    ["bla bla bla bla", True],
    ["Hi", False],
])
def test_three_words(words, expected):

    assert checkio(words) == expected


@pytest.mark.parametrize(["words", "res"], [
    [["how", "are", "you"], True],
    [["how", "1", "you"], False],
    [["2", "are", "you"], False],
    [["5", "2", "4"], False],
])
def test_all_words_are_text_check(words, res):
    assert all_words_are_text(words) == res

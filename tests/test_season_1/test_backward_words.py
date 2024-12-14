import pytest

from tasks.season_1.backward_words import (backward_string_by_word, reverse,
                                           backward_string_by_word_gen,
                                           backward_string_by_word_map)


@pytest.mark.parametrize("callable", [backward_string_by_word,
                                      backward_string_by_word_gen,
                                      backward_string_by_word_map])
@pytest.mark.parametrize(["text", "result"], [
    ['', ''],
    ['world', 'dlrow'],
    ['hello world', 'olleh dlrow'],
    ['hello   world', 'olleh   dlrow'],
    ['welcome to a game', 'emoclew ot a emag'],
])
def test_backward_words(callable, text, result):
    assert callable(text) == result


def test_reverse():
    assert reverse("123") == "321"
    assert reverse("") == ""

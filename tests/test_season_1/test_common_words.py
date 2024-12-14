import pytest
from tasks.season_1.common_words import checkio


@pytest.mark.parametrize(["item1", "item2", "res"], [
    ["hello,world", "hello,earth", "hello"],
    ["hello,world,hello", "hello,earth,hello", "hello"],
    ["one,two,three", "four,five,six", ""],
    ["one,two,three", "four,five,one,two,six,three", "one,three,two"],
])
def test_common_words(item1, item2, res):
    assert checkio(item1, item2) == res

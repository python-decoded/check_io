import pytest

from tasks.season_1.popular_words import (popular_words, popular_words_list,
                                          popular_words_comp, popular_words_perf,
                                          popular_words_all, popular_words_defaultdict,
                                          popular_words_counter)


@pytest.mark.parametrize("callable", [
    popular_words,
    popular_words_list,
    popular_words_comp,
    popular_words_perf,
    popular_words_all,
    popular_words_defaultdict,
    popular_words_counter])
def test_popular_words(callable):
    assert callable('''
    When I was One
    I had just begun
    When I was Two
    I was nearly new
    ''', ['i', 'was', 'three', 'near']) == {
            'i': 4,
            'was': 3,
            'three': 0,
            'near': 0
        }

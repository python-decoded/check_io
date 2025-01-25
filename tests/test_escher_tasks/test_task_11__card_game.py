import pytest

from tasks.escher_tasks.task_11__card_game import (
    cards, cards_while_loop, cards_for_loop)


@pytest.mark.parametrize("func", [cards, cards_while_loop, cards_for_loop])
@pytest.mark.parametrize("deck, hand, res", [
    (5, [2, 0, 1, 2], False),
    (10, [9, 9, 6, 6], True),
    (10, [11], False),
    (3, [0, 1, 1], False),
    (10, [3, 3, 5, 6, 6, 7], True),
    (8, [4, 4, 5, 6, 7], True),
    (7, [4, 4, 5, 6, 7], False),
    (4, [0, 0], False),
    (4, [2, 2], True),
    (4, [4, 4], False),
    (4, [2, 2, 2], False),
    (4, [1, 1, 2, 2], False),
    (4, [2, 2, 3, 3], False),
    (4, [0, 1, 2, 3, 3], False),
    (4, [1, 1, 2, 3, 4], False),
    (4, [0, 1, 2, 3, 4], False),
    (4, [1, 1, 2, 3, 3], False),
    (10, [1, 1, 2, 3, 4, 5, 6, 7, 7], False),
])
def test_cards(func, deck, hand, res):
    assert func(deck, hand) == res

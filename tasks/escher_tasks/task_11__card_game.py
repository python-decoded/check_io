def cards(deck: int, hand: list):

    hand = list(hand)
    extra = deck - len(hand)

    for i in range(deck):
        if i in hand:
            hand.remove(i)
        elif i + 1 in hand:
            hand.remove(i + 1)
        else:
            extra -= 1

        if extra < 0:
            return False

    return True


def cards_while_loop(deck: int, hand: list):

    hand = list(hand)

    while deck:
        if deck in hand:
            hand.remove(deck)
        elif deck - 1 in hand:
            hand.remove(deck - 1)

        deck -= 1

    return len(hand) == 0


def cards_for_loop(deck: int, hand: list):

    hand = list(hand)

    for i in range(deck, 0, -1):
        if i in hand:
            hand.remove(i)
        elif i - 1 in hand:
            hand.remove(i - 1)

    return len(hand) == 0

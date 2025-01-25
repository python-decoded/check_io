# https://py.checkio.org/mission/card-game/share/76bb61f050ce0b9c9f3f27a80f6bcaf9/


def cards(deck, hand):
    return True


if __name__ == '__main__':
    print("Example:")
    print(cards(5, [2, 0, 1, 2]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cards(5, [2, 0, 1, 2]) == False
    assert cards(10, [9, 9, 6, 6]) == True
    assert cards(10, [11]) == False
    assert cards(3, [0, 1, 1]) == False
    assert cards(10, [3, 3, 5, 6, 6, 7]) == True
    assert cards(8, [4, 4, 5, 6, 7]) == True
    assert cards(7, [4, 4, 5, 6, 7]) == False
    assert cards(4, [0, 0]) == False
    assert cards(4, [2, 2]) == True
    assert cards(4, [4, 4]) == False
    assert cards(4, [2, 2, 2]) == False
    assert cards(4, [1, 1, 2, 2]) == False
    assert cards(4, [2, 2, 3, 3]) == False
    assert cards(4, [0, 1, 2, 3, 3]) == False
    assert cards(4, [1, 1, 2, 3, 4]) == False
    assert cards(4, [0, 1, 2, 3, 4]) == False
    assert cards(4, [1, 1, 2, 3, 3]) == False
    assert cards(10, [1, 1, 2, 3, 4, 5, 6, 7, 7]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

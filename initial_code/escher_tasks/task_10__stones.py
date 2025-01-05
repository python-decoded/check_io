# https://py.checkio.org/mission/the-stones/share/7f88863914991d330224c416ab6c4905/


def stones(pile, moves):
    return 1


if __name__ == '__main__':
    print("Example:")
    print(stones(17, [1, 3, 4]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert stones(17, [1, 3, 4]) == 2
    assert stones(17, [1, 3, 4, 6, 9]) == 1
    assert stones(99, [1]) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")

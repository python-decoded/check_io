# https://py.checkio.org/mission/the-buttons/share/b137cafb218997a50c4ccf2d096f16ca/


def buttons(ceiling):
    #replace this for solution
    return 0


if __name__ == '__main__':
    print("Example:")
    print(buttons('''
001203
023001
100220'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert buttons('''
001203
023001
100220''') == [8, 4, 4, 1]

    assert buttons('''
000000
000055
000055''') == [20]

    assert buttons('''
908070
060504
302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

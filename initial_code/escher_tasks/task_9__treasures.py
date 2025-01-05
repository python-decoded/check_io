# https://py.checkio.org/mission/treasures/share/87fa2271940bde796baca58a08cf563e/

def treasures(info, limit):
    return []


if __name__ == '__main__':
    print("Example:")
    print(treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 200},
                     'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 1000},
                     'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5))

    assert treasures({'golden coin':
                          {'price': 100, 'weight': 50, 'amount': 200},
                      'silver coin':
                          {'price': 10, 'weight': 20, 'amount': 1000},
                      'ruby':
                          {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
               'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin':
                          {'price': 100, 'weight': 50, 'amount': 100},
                      'silver coin':
                          {'price': 10, 'weight': 20, 'amount': 100},
                      'ruby':
                          {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
               'golden coin: 100', 'silver coin: 100', 'ruby: 1']
    print("Coding complete? Click 'Check' to earn cool rewards!")

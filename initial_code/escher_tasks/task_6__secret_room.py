# https://py.checkio.org/mission/the-secret-room/share/e001f35ae056f4cb87d190c1127d6e2b/


def secret_room(number):
    return 0


if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")

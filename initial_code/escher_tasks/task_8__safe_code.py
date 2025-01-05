# https://py.checkio.org/mission/safe-code/share/69eff7293f27ff5514f60bb359a3ec38/


def safe_code(equation):
    return -1


if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")

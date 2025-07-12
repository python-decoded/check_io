# https://py.checkio.org/mission/the-tower/share/876370352bfd9cc7010d46fb9790c8dd/


def tower(cubes):
    return 0


if __name__ == "__main__":
    print("Example:")
    print(tower(["GYVABW", "AOCGYV", "CABVGO", "OVYWGA"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert tower(["GYVABW", "AOCGYV", "CABVGO", "OVYWGA"]) == 3
    assert tower(["ABCGYW", "CAYRGO", "OCYWBA", "ACYVBR", "GYVABW"]) == 1
    assert tower(["GYCABW", "GYCABW", "GYCABW", "GYCABW", "GYCABW"]) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")

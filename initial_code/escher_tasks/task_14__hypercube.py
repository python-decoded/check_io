# https://py.checkio.org/mission/hypercube/share/34afe6d58d340cb769045a7fedd5db44/


def hypercube(grid):
    return True


if __name__ == '__main__':
    print("Example:")
    print(hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]) == True
    assert hypercube([
              ['H', 'a', 't', 's', 'E'],
              ['a', 'Y', 'p', 'u', 'B'],
              ['a', 'a', 'P', 'y', 'U'],
              ['x', 'x', 'x', 'E', 'C'],
              ['z', 'z', 'z', 'z', 'R']]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

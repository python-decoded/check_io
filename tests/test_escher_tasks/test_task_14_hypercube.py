import pytest
from tasks.escher_tasks.task_14__hypercube import hypercube, hypercube_2


@pytest.mark.parametrize("func", [hypercube, hypercube_2])
def test_hypercube(func):

    assert func([
        ['g', 'f', 'H', 'Y', 'v'],
        ['z', 'e', 'a', 'P', 'u'],
        ['s', 'B', 'T', 'e', 'y'],
        ['k', 'u', 'c', 'R', 't'],
        ['l', 'O', 'k', 'p', 'r']]) == True

    assert func([
        ['H', 'a', 't', 's', 'E'],
        ['a', 'Y', 'p', 'u', 'B'],
        ['a', 'a', 'P', 'y', 'U'],
        ['x', 'x', 'x', 'E', 'C'],
        ['z', 'z', 'z', 'z', 'R']]) == False

    assert func([
        ['g', 'f', 'H', 'Y', 'p'],
        ['z', 'e', 'a', 'P', 'E'],
        ['s', 'B', 'T', 'e', 'y'],
        ['b', 'u', 'c', 'R', 't'],
        ['l', 'O', 'k', 'p', 'r']]) == True

    assert func([
        ['g', 'f', 'H', 'Y', 'v'],
        ['z', 'r', 'a', 'P', 'u'],
        ['s', 'B', 'T', 'e', 'y'],
        ['k', 'u', 'c', 'R', 't'],
        ['l', 'O', 'k', 'p', 'r']]) == False

from tasks.season_1.fizzbuzz import func


def test_fizzbuzz():
    assert func(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert func(6) == "Fizz", "6 is divisible by 3"
    assert func(5) == "Buzz", "5 is divisible by 5"
    assert func(7) == "7", "7 is not divisible by 3 or 5"


def test_fizzbuzz_1():
    assert func(15) == "Fizz Buzz", "15 is divisible by 3 and 5"


def test_fizzbuzz_2():
    assert func(6) == "Fizz", "6 is divisible by 3"


def test_fizzbuzz_3():
    assert func(5) == "Buzz", "5 is divisible by 5"


def test_fizzbuzz_4():
    assert func(7) == "7", "7 is not divisible by 3 or 5"

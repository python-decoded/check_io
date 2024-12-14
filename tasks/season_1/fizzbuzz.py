def func(number: int) -> str:

    res = str(number)

    if number % 15 == 0:
        res = "Fizz Buzz"
    elif number % 5 == 0:
        res = "Buzz"
    elif number % 3 == 0:
        res = "Fizz"

    return res

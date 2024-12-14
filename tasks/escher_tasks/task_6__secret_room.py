ONES = ["zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"]

TENS = ["twenty", "thirty", "forty",
        "fifty", "sixty", "seventy",
        "eighty", "ninety"]


def translated(number):
    assert number <= 1000, "number > 1000"

    if number == 1000:
        return "one thousand"
    if number == 0:
        return "zero"

    hundred, other = divmod(number, 100)
    ten, one = divmod(other, 10)

    res = []
    res.append(f"{ONES[hundred]} hundred") if hundred else None
    res.append(ONES[other]) if other in range(1, 20) else None
    res.append(TENS[ten - 2]) if other >= 20 else None
    res.append(ONES[one]) if other >= 20 and one else None
    return " ".join(res)


def secret_room(number):
    numbers = list(range(1, number + 1))
    numbers = [translated(n) for n in numbers]
    numbers = sorted(numbers)
    return numbers.index(translated(number)) + 1

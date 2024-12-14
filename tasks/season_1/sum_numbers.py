def sum_numbers(text: str) -> int:

    res = 0

    words = text.split(" ")
    for word in words:
        if word.lstrip("-").isdecimal():
            res += int(word)

    return res

def checkio(first, second):
    first = set(first.split(","))
    second = set(second.split(","))

    res = first.intersection(second)
    return ",".join(sorted(res))

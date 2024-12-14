def checkio(data: list) -> list:

    res = []

    for i in data:
        if data.count(i) > 1:
            res.append(i)

    return res


def checkio_gen(data: list) -> list:
    return list(i for i in data if data.count(i) > 1)


def checkio_list_comp(data: list) -> list:
    return [i for i in data if data.count(i) > 1]


def checkio_filter(data: list) -> list:
    not_unique = lambda item: data.count(item) > 1
    return list(filter(not_unique, data))

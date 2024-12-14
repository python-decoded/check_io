def is_leaf(array):
    return isinstance(array, int)


def flat_list(array):
    res = []

    for i in array:
        if is_leaf(i):
            res.append(i)
        else:
            leafs = flat_list(i)
            res += leafs

    return res


def flat_list_while(array):
    res = []

    query = list(array)

    while query:
        i = query.pop(0)
        if is_leaf(i):
            res.append(i)
        else:
            items = list(i)
            query = items + query

    return res

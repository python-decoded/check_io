def treasures(info, limit):

    limit = int(limit * 1000)
    keys = sorted(info,
                  key=lambda k: info[k]["price"] / info[k]["weight"],
                  reverse=True)

    res = {}
    for k in keys:
        can_take = limit // info[k]["weight"]
        will_take = min(can_take, info[k]["amount"])
        res[k] = will_take
        limit -= will_take * info[k]["weight"]

    return [f"{k}: {res[k]}" for k in info if res[k] > 0]


from itertools import product


def treasures_2(info, limit):

    limit = int(limit * 1000)

    counts = {}
    for k in info:
        can_put = limit // info[k]["weight"]
        will_put = min(can_put, info[k]["amount"])
        counts[k] = will_put

    res = [0 for _ in info]
    best_price = 0

    for combination in product(*[range(counts[k] + 1) for k in info]):
        total_price = sum([amount * info[k]["price"]
                           for k, amount in zip(info, combination)])
        total_weight = sum([amount * info[k]["weight"]
                            for k, amount in zip(info, combination)])

        if total_weight <= limit and total_price > best_price:
            res = combination
            best_price = total_price

    return [f"{k}: {count}" for k, count in zip(info, res) if count]


def treasures_3(info, limit):

    limit = int(limit * 1000)
    best_results = [[0 for _ in info]]

    for i in range(1, limit + 1):
        results = [best_results[-1].copy()]

        for _idx, k in enumerate(info):
            if i < info[k]["weight"]:
                continue

            res = best_results[i - info[k]["weight"]].copy()
            res[_idx] += 1
            if res[_idx] > info[k]["amount"]:
                continue
            results.append(res)

        get_price = lambda res: sum(i * info[k]["price"]
                                    for i, k in zip(res, info))
        best_results.append(max(results, key=get_price))

    return [f"{k}: {i}" for k, i in zip(info, best_results[-1]) if i]

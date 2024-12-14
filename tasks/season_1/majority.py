def is_majority(items: list) -> bool:

    true_count = 0
    false_count = 0

    for i in items:
        if i is True:
            true_count += 1
        else:
            false_count += 1

    return true_count > false_count


def is_majority_count(items) -> bool:
    true_count = items.count(True)
    false_count = items.count(False)
    return true_count > false_count


def is_majority_len(items) -> bool:
    true_count = items.count(True)
    return true_count * 2 > len(items)


def is_majority_sum(items) -> bool:
    true_count = sum(items)
    return true_count * 2 > len(items)


def is_majority_agg(items) -> bool:
    return sum([-1, 1][i] for i in items) > 0


# works for python 3.10+
# def is_majority_match_case(items) -> bool:
#
#     total = 0
#
#     for i in items:
#
#         match i:
#             case True:
#                 res = 1
#             case _:
#                 res = -1
#
#         total += res
#
#     return total > 0

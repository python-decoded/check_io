def as_table(data: str) -> list:
    rows = data.splitlines()
    return [list(r.strip()) for r in rows if r.strip()]


def cut(table: list) -> list:
    while table and "#" not in table[0]:
        table = table[1:]
    while table and "#" not in table[-1]:
        table = table[:-1]
    while table and "#" not in list(zip(*table))[0]:
        table = [row[1:] for row in table]
    while table and "#" not in list(zip(*table))[-1]:
        table = [row[:-1] for row in table]
    return table


def rotate(table: list) -> list:

    data = list(zip(*table))
    return [list(r[::-1]) for r in data]


def keys_and_locks(lock, some_key):

    lock = cut(as_table(lock))
    some_key = cut(as_table(some_key))
    some_key_2 = rotate(some_key)
    some_key_3 = rotate(some_key_2)
    some_key_4 = rotate(some_key_3)

    return lock in [some_key, some_key_2, some_key_3, some_key_4]

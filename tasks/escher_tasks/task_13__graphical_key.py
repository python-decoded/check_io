from itertools import chain

NEIGHBOURS = [(1, 0), (0, 1), (-1, 0), (0, -1),
              (1, 1), (-1, 1), (-1, -1), (1, -1)]


def g_key(grid, path):
    """
    Рішення з використанням динамічного програмування
    Ефективне рішення,
    Але не надає найкращі результати
    """

    h, w = len(grid), len(grid[0])
    results = {(0, 0): [[0, 0]]}

    get_path_total = lambda path: sum(grid[y][x] for x, y in path)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):

            best_path = []

            for dx, dy in NEIGHBOURS:
                path_key = x + dx, y + dy
                if path_key not in results:
                    continue

                new_path = results[path_key] + [[x, y]]

                # can still reach end
                if max(h - y, w - x) + len(new_path) > path:
                    continue

                # path is better than best path
                best_path = max(new_path, best_path, key=get_path_total)

            if best_path:
                results[(x, y)] = best_path

    return get_path_total(results[(x, y)])


def g_key(grid, path):

    best_possible = sum(sorted(chain.from_iterable(grid),
                               reverse=True)[:path])

    h, w = len(grid), len(grid[0])
    best_path = []
    all_paths = [
        [(0, 0)]
    ]
    visited = set()
    path_total = lambda path: sum(grid[y][x] for x, y in path)
    skipped = 0

    while all_paths:
        current_path = all_paths.pop(0)
        x, y = current_path[-1]

        for dx, dy in NEIGHBOURS:
            _x, _y = x + dx, y + dy

            if (_x, _y) in current_path:
                continue
            if _x not in range(w) or _y not in range(h):
                continue

            new_path = current_path + [(_x, _y)]

            if new_path in all_paths:
                continue
            if len(new_path) > path:
                continue

            if (frozenset(new_path), (_x, _y)) in visited:
                skipped += 1
                continue
            visited.add((frozenset(new_path), (_x, _y)))

            if (_x, _y) != (w - 1, h - 1):
                all_paths.insert(0, new_path)
                continue

            best_path = max(best_path, new_path, key=path_total)
            if path_total(best_path) == best_possible:
                return best_possible

    return path_total(best_path)

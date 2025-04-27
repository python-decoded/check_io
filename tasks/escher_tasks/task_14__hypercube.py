NEIGHBOURS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def hypercube(grid, word="hypercube") -> bool:

    h, w = len(grid), len(grid[0])
    paths = [[(x, y)]
             for x in range(w)
             for y in range(h)
             if grid[y][x].lower() == word[0]]

    while paths:
        path = paths.pop(0)
        *body, (x, y) = path
        expected_letter = word[len(path)].lower()

        for dx, dy in NEIGHBOURS:
            _x, _y = x + dx, y + dy
            if (_x, _y) in path:
                continue
            if _x not in range(w) or _y not in range(h):
                continue

            if grid[_y][_x].lower() != expected_letter:
                continue
            if len(path) + 1 == len(word):
                return True

            paths.insert(0, path + [(_x, _y)])

    return False


def hypercube_2(grid, word="hypercube") -> bool:

    h, w = len(grid), len(grid[0])
    paths = [[(x, y)]
             for x in range(w)
             for y in range(h)
             if grid[y][x].lower() == word[0]]

    for expected_letter in word[1:]:

        new_paths = []

        for path in paths:
            *body, (x, y) = path

            for dx, dy in NEIGHBOURS:
                _x, _y = x + dx, y + dy
                if (_x, _y) in path:
                    continue
                if _x not in range(w) or _y not in range(h):
                    continue

                if grid[_y][_x].lower() != expected_letter:
                    continue

                new_paths.append(path + [(_x, _y)])

        paths = new_paths

    return len(paths) > 0

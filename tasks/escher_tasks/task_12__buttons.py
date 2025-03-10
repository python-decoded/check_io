def get_group(matrix: list[str], item: tuple[int, int]) -> set:

    to_visit = {item}
    visited = set()
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while to_visit:
        x, y = to_visit.pop()
        visited.add((x, y))

        for dx, dy in deltas:
            if y + dy not in range(len(matrix)):
                continue
            if x + dx not in range(len(matrix[0])):
                continue

            if matrix[y + dy][x + dx] == "0":
                continue
            if (x + dx, y + dy) in visited:
                continue

            to_visit.add((x + dx, y + dy))

    return visited


def buttons(ceiling: str):

    matrix = [line.strip()
              for line in ceiling.splitlines()
              if line.strip()]

    groups = []
    visited = set()

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if (x, y) in visited:
                continue
            if cell == "0":
                continue

            group: set = get_group(matrix, (x, y))
            visited.update(group)
            group_weight = sum(int(matrix[y][x])
                               for x, y in group)
            groups.append(group_weight)

    return sorted(groups, reverse=True)


def buttons_2(ceiling: str):

    matrix = [line.strip()
              for line in ceiling.splitlines()
              if line.strip()]
    height, width = len(matrix), len(matrix[0])
    to_visit = {(x, y)
                for x in range(width)
                for y in range(height)
                if matrix[y][x] != "0"}

    groups = []

    while to_visit:
        x, y = to_visit.pop()
        group: set = get_group(matrix, (x, y))
        group_weight = sum(int(matrix[y][x]) for x, y in group)
        groups.append(group_weight)
        to_visit -= group

    return sorted(groups, reverse=True)

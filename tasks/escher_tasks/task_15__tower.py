def rotate(cube, directions):

    for direction in directions:
        if direction == "x":
            cube = cube[4] + cube[1] + cube[2] + cube[5] + cube[3] + cube[0]
        elif direction == "y":
            cube = cube[2] + cube[0] + cube[3] + cube[1] + cube[4] + cube[5]
        elif direction == "z":
            cube = cube[0] + cube[5] + cube[4] + cube[3] + cube[1] + cube[2]
    return cube


def get_combinations(cube):
    all_sides = [
        cube,
        rotate(cube, "y"),
        rotate(cube, "yy"),
        rotate(cube, "yyy"),
        rotate(cube, "x"),
        rotate(cube, "xxx"),
    ]
    res = []

    for side in all_sides:
        res += [side,
                rotate(side, "z"),
                rotate(side, "zz"),
                rotate(side, "zzz")]

    return res


def tower(cubes):

    all_combinations = []
    for cube in cubes:
        all_combinations.extend(
            {c[:4] for c in get_combinations(cube)})

    best = max(all_combinations, key=all_combinations.count)
    return all_combinations.count(best)


def tower2(cubes):
    INDEXES = {'3540', '1032', '2031', '5124', '3210',
               '5034', '1542', '5304', '4215', '5214',
               '0123', '2541', '1302', '4125', '2301',
               '1452', '0213', '2451', '0543', '3450',
               '4305', '0453', '3120', '4035'}

    all_combinations = []
    for cube in cubes:
        combinations = {"".join(cube[int(_idx)] for _idx in i)
                        for i in INDEXES}
        all_combinations.extend(combinations)

    best = max(all_combinations, key=all_combinations.count)
    return all_combinations.count(best)

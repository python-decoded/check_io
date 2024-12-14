def stone_wall_1(wall):

    wall = [row for row in wall.splitlines() if row]
    cols = list(zip(*wall))
    get_compare_val = lambda index: cols[index].count("#")
    return min(range(len(cols)), key=get_compare_val)


def stone_wall_2(wall):

    wall = [row for row in wall.splitlines() if row]
    values = [col.count("#") for col in zip(*wall)]
    return min(range(len(values)), key=values.__getitem__)

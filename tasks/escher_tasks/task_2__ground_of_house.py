def house(plan):

    plan = [i for i in plan.splitlines() if i]

    height = len(plan)
    width = len(plan[0])

    for up in range(height):
        if "#" in plan[up]:
            break

    for down in range(height)[::-1]:
        if "#" in plan[down]:
            break

    rotated_plan = list(zip(*plan))

    for left in range(width):
        if "#" in rotated_plan[left]:
            break

    for right in range(width)[::-1]:
        if "#" in rotated_plan[right]:
            break

    return (right - left + 1) * (down - up + 1)


def house_2(plan):

    rows = [r for r in plan.splitlines() if r]
    cols = list(zip(*rows))

    height = len("".join("#" if "#" in i else "0" for i in rows).strip("0"))
    width = len("".join("#" if "#" in i else "0" for i in cols).strip("0"))

    return height * width

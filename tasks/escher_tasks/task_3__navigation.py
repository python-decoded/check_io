def navigation(seaside):

    positions = {}

    for y, row in enumerate(seaside):
        for x, cell in enumerate(row):
            if isinstance(cell, str):
                positions[cell] = (x, y)

    x1, y1 = positions.pop("Y")
    return sum(max(abs(x1 - x2), abs(y1 - y2))
               for x2, y2 in positions.values())

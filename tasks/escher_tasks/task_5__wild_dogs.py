import math
from itertools import combinations

# geometry helpers
type Point = tuple[int | float, int | float]


def is_collinear(p1: Point, p2: Point, p3: Point) -> bool:
    """
    Функція отримує на вхід координати 3х точок,
    і визначає, чи вони знаходяться на одній прямій
    """
    return ((p1[1] - p2[1]) * (p1[0] - p3[0])
            == (p1[1] - p3[1]) * (p1[0] - p2[0]))


def line_get_distance_to_point(line: tuple[Point, Point], point: Point) -> float:
    """
    Функція визначає довжину перпендикуляру
    опущеного з точки на лінію проведену через 2 точки
    """

    (p1, p2), p3 = line, point
    nom = abs((p2[0] - p1[0]) * (p1[1] - p3[1]) - (p1[0] - p3[0]) * (p2[1] - p1[1]))
    denom = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return nom / denom


def wild_dogs(coords):

    res = []

    for p1, p2 in combinations(coords, 2):
        line = p1, p2
        count = sum(p in line or is_collinear(*line, p) for p in coords)
        distance = round(line_get_distance_to_point(line, (0, 0)), 2)

        res.append([-count, distance])

    return min(res)[1]

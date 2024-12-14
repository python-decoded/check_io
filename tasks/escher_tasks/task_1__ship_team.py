from bisect import insort_left

def two_teams(sailors):
    ships = [[],[]]
    for sailor, age in sailors.items():
        insort_left(ships[20 <= age <= 40], sailor)
    return ships

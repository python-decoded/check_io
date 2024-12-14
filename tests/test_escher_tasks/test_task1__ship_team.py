from tasks.escher_tasks.task_1__ship_team import two_teams


def test_two_teams():

    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
               ['Abrahams', 'Coleman'],
               ['Smith', 'Wesson']
           ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
               ['Fernandes', 'Kale', 'McCortney'],
               ['Johnson']
           ]

    assert two_teams({'Samuelson': 19.99, 'Besson': 28, 'Rick': 39.95, 'Wayfarer': 40.1}) == [
        ['Samuelson', 'Wayfarer'],
        ['Besson', 'Rick']
    ]

    assert two_teams({'Pitty': 19, 'Wolf': 40.005, 'Doberman': 42, 'Bobber': 18}) == [
        ['Bobber', 'Doberman', 'Pitty', 'Wolf'],
        []
    ]

    assert two_teams({'Carlos': 34, 'Richardson': 20, 'Dow': 40}) == [
        [],
        ['Carlos', 'Dow', 'Richardson']
    ]

    assert two_teams({'Dave': 24}) == [
        [],
        ['Dave']
    ]

    assert two_teams({'Hubert': 38.3, 'Barney': 31, 'Kirk': 42.5, 'Lion': 56}) == [
        ['Kirk', 'Lion'],
        ['Barney', 'Hubert']
    ]

    assert two_teams({'Sam': 19}) == [
        ['Sam'],
        []
    ]

    assert two_teams( {'Karl': 17, 'Richard': 20, 'Dantes': 39, 'Fargo': 19}) == [
        ['Fargo', 'Karl'],
        ['Dantes', 'Richard']
    ]

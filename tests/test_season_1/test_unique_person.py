from datetime import datetime

import pytest

from tasks.season_1.unique_person import Person


def test_person_date():
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600,
                "Canada", "Vancouver", "male")
    assert p1.birth_date == datetime(1979, 9, 19)


def test_person_name():
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600,
                "Canada", "Vancouver", "male")
    assert p1.name() == "John Smith"


@pytest.mark.parametrize(["birth_date", "age"], [
    ["01.01.2010", 8],
    ["02.01.2010", 7],
    ["31.12.2009", 8],
])
def test_person_age(birth_date, age):
    p1 = Person("John", "Smith", birth_date, "welder", 15, 3600,
                "Canada", "Vancouver", "male")
    assert p1.age() == age


def test_person_1():
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600,
                "Canada", "Vancouver", "male")

    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p1.money() == "648 000", "Money"
    assert p1.work() == "He is a welder", "Job"


def test_person_2():
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150,
                "Austria", "Vienna")

    assert p2.work() == "Is a designer", "Job"
    assert p2.home() == "Lives in Vienna, Austria", "Home"


def test_person_3():
    p1 = Person("Ann", "Smith", "19.09.1979", "welder", 15, 3600,
                "Canada", "Vancouver", "female")

    assert p1.name() == "Ann Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p1.money() == "648 000", "Money"
    assert p1.work() == "She is a welder", "Job"

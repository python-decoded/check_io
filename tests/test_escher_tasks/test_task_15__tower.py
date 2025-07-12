from tasks.escher_tasks.task_15__tower import tower, tower2


def test_tower():
    assert tower(["GYVABW", "AOCGYV", "CABVGO", "OVYWGA"]) == 3
    assert tower(["ABCGYW", "CAYRGO", "OCYWBA", "ACYVBR", "GYVABW"]) == 1
    assert tower(["GYCABW", "GYCABW", "GYCABW", "GYCABW", "GYCABW"]) == 5


def test_tower2():
    assert tower2(["GYVABW", "AOCGYV", "CABVGO", "OVYWGA"]) == 3
    assert tower2(["ABCGYW", "CAYRGO", "OCYWBA", "ACYVBR", "GYVABW"]) == 1
    assert tower2(["GYCABW", "GYCABW", "GYCABW", "GYCABW", "GYCABW"]) == 5

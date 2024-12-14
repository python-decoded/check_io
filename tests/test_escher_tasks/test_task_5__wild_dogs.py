from tasks.escher_tasks.task_5__wild_dogs import wild_dogs


def test_wild_dogs():

    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

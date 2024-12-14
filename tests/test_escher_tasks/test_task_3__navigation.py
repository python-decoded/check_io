from tasks.escher_tasks.task_3__navigation import navigation


def test_navigation():

    assert navigation([['Y', 0, 0, 0, 'C'],
                       [0,  0, 0, 0,  0],
                       [0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[0,  0, 'C'],
                       [0, 'S', 0],
                       ['M', 'Y', 0]]) == 4

    assert navigation([[0,  0, 0,  0,  0,  0,  0],
                       [0,  0, 0, 'M', 0, 'S', 0],
                       [0,  0, 0,  0,  0,  0,  0],
                       [0,  0, 0, 'C', 0,  0,  0],
                       [0, 'Y', 0,  0,  0,  0,  0],
                       [0,  0, 0,  0,  0,  0,  0]]) == 9

from tasks.escher_tasks.task_7__keys_and_locks import (keys_and_locks, cut,
                                                       rotate, as_table)


def test_as_table():
    data = """
    #0#
    ###
    """
    assert as_table(data) == [["#", "0", "#"],
                              ["#", "#", "#"]]


def test_cut():
    data = [["#", "0"],
            ["#", "0"]]
    res = [["#"],
           ["#"]]
    assert cut(data) == res

    data = [["#", "#"],
            ["0", "0"]]
    res = [["#", "#"]]
    assert cut(data) == res


def test_rotate():
    data = [["#", "0"],
            ["#", "0"],
            ["0", "#"]]
    res = [["0", "#", "#"],
           ["#", "0", "0"]]
    assert rotate(data) == res


def test_keys_and_locks():

    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False

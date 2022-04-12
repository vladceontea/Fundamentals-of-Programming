"""
Assemble the program and start the user interface here
"""

from src.domain.entity import create_contestant, get_p1, get_p2, get_p3
from src.functions.functions import mean_score, add_contestant, insert_contestant, remove_contestant, remove_multiple_contestant, replace_contestant, display_list, sorted_list, split_command, average, minimum, top_contestants, top_contestants_score, remove_compare
from src.ui.console import show_list_ui, add_contestant_ui, remove_contestant_ui, insert_contestant_ui, replace_contestant_ui, average_ui, minimum_ui, top_contestants_ui, undo_ui


def start_command_ui():
    contestant_list = []
    history_list = []
    test_init(contestant_list)
    command_dict = {'list': show_list_ui, 'add': add_contestant_ui, 'remove': remove_contestant_ui, 'insert': insert_contestant_ui, 'replace': replace_contestant_ui, 'avg': average_ui, 'min': minimum_ui, 'top': top_contestants_ui}
    done = False
    while not done:
        command = input('command: ')
        try:
            cmd_word, cmd_params = split_command(command)
            if cmd_word in command_dict:
                command_dict[cmd_word](contestant_list, cmd_params, history_list)
            elif cmd_word == 'undo':
                contestant_list, history_list = undo_ui(contestant_list, cmd_params, history_list)
            elif cmd_word == 'exit':
                done = True
            else:
                print('Invalid command')
        except ValueError as ve:
            print(str(ve))


def test_init(contestant_list):
    contestant_list.append(create_contestant(3, 7, 8))
    contestant_list.append(create_contestant(4, 8, 8))
    contestant_list.append(create_contestant(2, 6, 10))
    contestant_list.append(create_contestant(1, 2, 1))
    contestant_list.append(create_contestant(6, 7, 5))
    contestant_list.append(create_contestant(9, 10, 9))
    contestant_list.append(create_contestant(3, 7, 2))
    contestant_list.append(create_contestant(4, 2, 8))
    contestant_list.append(create_contestant(7, 10, 9))
    contestant_list.append(create_contestant(1, 3, 5))


def test_create_contestant():
    c = create_contestant(1, 8, 6)
    assert get_p1(c) == 1 and get_p2(c) == 8 and get_p3(c) == 6
    try:
        c = create_contestant(2, 7, 12)
        assert False
    except ValueError:
        assert True


def test_mean_score():
    c = create_contestant(5, 8, 9)
    assert mean_score(c) == 7.333333333333333


def test_add_contestant():
    contestant_list = []
    test_init(contestant_list)
    c = create_contestant(2, 6, 8)
    add_contestant(contestant_list, c)
    assert len(contestant_list) == 11


def test_insert_contestant():
    contestant_list = []
    test_init(contestant_list)
    c = create_contestant(2, 6, 8)
    insert_contestant(contestant_list, c, 4)
    assert contestant_list[4] == [2, 6, 8] and len(contestant_list) == 11


def test_remove_contestant():
    contestant_list = []
    test_init(contestant_list)
    remove_contestant(contestant_list, 3)
    assert contestant_list[3] == [0, 0, 0]


def test_remove_multiple_contestant():
    contestant_list = []
    test_init(contestant_list)
    remove_multiple_contestant(contestant_list, 2, 5)
    assert contestant_list[2] == [0, 0, 0] and contestant_list[3] == [0, 0, 0] and contestant_list[4] == [0, 0, 0] and contestant_list[5] == [0, 0, 0]


def test_replace_contestant():
    contestant_list = []
    test_init(contestant_list)
    replace_contestant(contestant_list, 3, 4, 'P1')
    assert contestant_list[3] == [4, 2, 1]


def test_display_list():
    contestant_list = []
    test_init(contestant_list)
    new_list = display_list(contestant_list, '=', 3)
    assert new_list == [[1, 3, 5]]


def test_sorted_list():
    contestant_list = []
    test_init(contestant_list)
    new_list, k = sorted_list(contestant_list)
    assert new_list[0] == [9, 10, 9], k[0] == 5


def test_remove_compare():
    contestant_list = []
    test_init(contestant_list)
    remove_compare(contestant_list, '<', 20)
    assert contestant_list[3] == [0, 0, 0]


def test_top_contestants_score():
    contestant_list = []
    test_init(contestant_list)
    new_list, k, m = top_contestants_score(contestant_list, 2, 'P2')
    assert m[0] == 10 and m[1] == 10


def test_top_contestants():
    contestant_list = []
    test_init(contestant_list)
    new_list, k, m = top_contestants(contestant_list, 2)
    assert new_list[0] == [9, 10, 9] and new_list[1] == [7, 10, 9]


def test_minimum():
    contestant_list = []
    test_init(contestant_list)
    value = minimum(contestant_list, 7, 9)
    assert value == 3


def test_average():
    contestant_list = []
    test_init(contestant_list)
    value = average(contestant_list, 9, 9)
    assert value == 3


test_create_contestant()
test_mean_score()
test_add_contestant()
test_insert_contestant()
test_remove_contestant()
test_remove_multiple_contestant()
test_replace_contestant()
test_display_list()
test_sorted_list()
test_remove_compare()
test_top_contestants_score()
test_top_contestants()
test_minimum()
test_average()

start_command_ui()

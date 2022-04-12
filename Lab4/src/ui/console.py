"""
This is the user interface module. These functions call functions from the domain and functions module.
"""
import copy
from src.domain.entity import create_contestant, to_str
from src.functions.functions import add_contestant, insert_contestant, remove_contestant, remove_multiple_contestant, replace_contestant, display_list, sorted_list, average, minimum, top_contestants, top_contestants_score, remove_compare, undo


def insert_contestant_ui(contestant_list, cmd_params, history_list):
    new_list = copy.deepcopy(contestant_list)
    history_list.append(new_list)
    tokens = cmd_params.split(' ')
    if len(tokens) != 5:
        raise ValueError('Invalid parameter count')

    if tokens[3] != 'at':
        raise ValueError('Wrong syntax')

    if int(tokens[4]) > len(contestant_list):
        raise ValueError('Cannot add at this position')

    contestant = create_contestant(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    insert_contestant(contestant_list, contestant, int(tokens[4]))
    print('Successfully added a new contestant')


def add_contestant_ui(contestant_list, cmd_params, history_list):
    new_list = copy.deepcopy(contestant_list)
    history_list.append(new_list)
    tokens = cmd_params.split(' ')

    if len(tokens) != 3:
        raise ValueError('Invalid parameter count')

    contestant = create_contestant(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    add_contestant(contestant_list, contestant)
    print('Successfully added a new contestant')


def remove_contestant_ui(contestant_list, cmd_params, history_list):
    new_list = copy.deepcopy(contestant_list)
    history_list.append(new_list)
    tokens = cmd_params.split(' ')
    if len(tokens) > 3:
        raise ValueError('Invalid parameter count')

    if len(tokens) == 1:
        remove_contestant(contestant_list, int(tokens[0]))
    elif tokens[1] != 'to' and tokens[0] != '<' and tokens[0] != '>':
        raise ValueError('Wrong syntax')
    elif len(tokens) == 2:
        remove_compare(contestant_list, tokens[0], int(tokens[1]))
    else:
        remove_multiple_contestant(contestant_list, int(tokens[0]), int(tokens[2]))
    print('Successfully set the scores to 0')


def replace_contestant_ui(contestant_list, cmd_params, history_list):
    new_list = copy.deepcopy(contestant_list)
    history_list.append(new_list)
    tokens = cmd_params.split(' ')
    if len(tokens) != 4:
        raise ValueError('Invalid parameter count')

    if tokens[2] != 'with':
        raise ValueError('Wrong syntax')

    if tokens[1] != 'P1' and tokens[1] != 'P2' and tokens[1] != 'P3':
        raise ValueError('Wrong syntax')

    replace_contestant(contestant_list, int(tokens[0]), int(tokens[3]), tokens[1])
    print('Successfully modified the score')


def average_ui(contestant_list, cmd_params, history_list):
    tokens = cmd_params.split(' ')
    if len(tokens) != 3:
        raise ValueError('Invalid parameter count')
    if int(tokens[0]) < 0 or int(tokens[2]) > len(contestant_list)-1:
        raise ValueError('Not a valid interval')

    if tokens[1] != 'to':
        raise ValueError('Wrong syntax')
    else:
        print('The average of these scores is ' + str(average(contestant_list, int(tokens[0]), int(tokens[2]))))


def minimum_ui(contestant_list, cmd_params, history_list):
    tokens = cmd_params.split(' ')
    if len(tokens) != 3:
        raise ValueError('Invalid parameter count')
    if int(tokens[0]) < 0 or int(tokens[2]) > len(contestant_list)-1:
        raise ValueError('Not a valid interval')

    if tokens[1] != 'to':
        raise ValueError('Wrong syntax')
    else:
        print('The minimum average score is ' + str(minimum(contestant_list, int(tokens[0]), int(tokens[2]))))


def top_contestants_ui(contestant_list, cmd_params, history_list):
    tokens = cmd_params.split(' ')
    if len(tokens) > 2:
        raise ValueError('Invalid parameter count')

    if int(tokens[0]) > len(contestant_list):
        raise ValueError('There are not this many contestants')

    if len(tokens) == 1:
        contestant_list, k, m = top_contestants(contestant_list, int(tokens[0]))
        i = 0
        for contestant in contestant_list:
            print('Contestant number ' + str(k[i]) + ' with the score ' + str(m[i]))
            i = i + 1
    elif tokens[1] != 'P1' and tokens[1] != 'P2' and tokens[1] != 'P3':
        raise ValueError('Wrong syntax')
    else:
        contestant_list, k, m = top_contestants_score(contestant_list, int(tokens[0]), tokens[1])
        i = 0
        for contestant in contestant_list:
            print('Contestant number ' + str(k[i]) + ' with the score ' + str(m[i]))
            i = i + 1


def undo_ui(contestant_list, cmd_params, history_list):
    if len(history_list) == 0:
        raise ValueError('There is no operation to undo')
    if not cmd_params:
        contestant_list, history_list = undo(contestant_list, history_list)
    else:
        raise ValueError('Invalid parameter count')
    return contestant_list, history_list


def show_list_ui(contestant_list, cmd_params, history_list):
    if not cmd_params:
        i = 0
        for contestant in contestant_list:
            print(to_str(i, contestant))
            i = i + 1
    else:
        tokens = cmd_params.split(' ')
        if len(tokens) != 1 and len(tokens) != 2:
            raise ValueError('Invalid parameter count')

        if(tokens[0]) == 'sorted':
            i = 0
            contestant_list, k = sorted_list(contestant_list)
            for contestant in contestant_list:
                print(to_str(k[i], contestant))
                i = i + 1
        elif tokens[0] == '=' or tokens[0] == '<' or tokens[0] == '>':
            new_list = display_list(contestant_list, tokens[0], int(tokens[1]))
            if len(new_list) == 0:
                print('Empty list')
            i = 0
            for contestant in contestant_list:
                if contestant in new_list:
                    print(to_str(i, contestant))
                i = i + 1
        else:
            raise ValueError('Wrong syntax')

#
# Write the implementation for A3 in this file
#

#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)

def create_contestant(p1, p2, p3):
    """
    Create contestant with given parameters
    :param p1: score of p1
    :param p2: score of p2
    :param p3: score of p3
    """
    # print(type(student_id)) -> what's my type?
    if p1 < 0 or p1 > 10 or p2 < 0 or p2 > 10 or p3 < 0 or p3 > 10:
        raise ValueError('Cannot create contestant using given arguments')
    return [p1, p2, p3]


def get_p1(contestant):
    return contestant[0]


def get_p2(contestant):
    return contestant[1]


def get_p3(contestant):
    return contestant[2]


def to_str(index, contestant):
    """
    Build the str representation for a contestant
    :param index: the index of the contestant
    :param contestant: The contestant
    :return: Its str representation
    """
    return 'Contestant number ' + str(index) + ': ' + str(get_p1(contestant)) + ' ' + str(get_p2(contestant)) + ' ' + str(get_p3(contestant))


# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values

def mean_score(contestant):
    """
    Calculates the mean score of the problems
    :param contestant: The contestant
    :return: The mean score
    """
    mean = (get_p1(contestant) + get_p2(contestant) + get_p3(contestant))/3
    return mean


def add_contestant(contestant_list, contestant):
    """
    Adds contestant to the list
    :param contestant_list: The list of all contestants
    :param contestant: The new contestant
    :return: -
    """
    contestant_list.append(contestant)


def insert_contestant(contestant_list, new_contestant, position):
    """
    Add contestant to the list on a certain position
    :param contestant_list: The list of all contestants
    :param new_contestant: The new contestant
    :param position: The position of the new contestant
    :return: -
    """
    contestant_list.append(create_contestant(0, 0, 0))
    for i in range(len(contestant_list)-1, position, -1):
        contestant_list[i] = contestant_list[i-1]
    contestant_list[position] = new_contestant


def remove_contestant(contestant_list, removed_contestant):
    """
    Sets the contestant's results to 0
    :param contestant_list: The list of all contestants
    :param removed_contestant: The contestant that is removed
    :return: -
    """
    i = 0
    for contestant in contestant_list:
        if i == removed_contestant:
            contestant[0] = 0
            contestant[1] = 0
            contestant[2] = 0
        i = i + 1


def remove_multiple_contestant(contestant_list, first_contestant, second_contestant):
    """
    Sets multiple contestants' results to 0
    :param contestant_list: The list of all contestants
    :param first_contestant: The position of hte first contestants that is removed
    :param second_contestant: The position of the last contestant that is removed
    :return: -
    """
    i = 0
    for contestant in contestant_list:
        if first_contestant <= i <= second_contestant:
            contestant[0] = 0
            contestant[1] = 0
            contestant[2] = 0
        i = i + 1


def replace_contestant(contest_list, position, new_score, problem):
    """
    Replaces the score of a contestant's problem with a certain value
    :param contest_list: The list of all contestants
    :param position: The position of the contestant
    :param new_score: The new score
    :param problem: The problem number
    :return: -
    """
    i = 0
    if problem == 'P1':
        number = 0
    elif problem == 'P2':
        number = 1
    else:
        number = 2
    for contestant in contest_list:
        if i == position:
            contestant[number] = new_score
        i = i + 1


def display_list(contestant_list, operation, average_score):
    """
    Displays the filtered list
    :param contestant_list: The list of all contestants
    :param operation: The operation by which it filters
    :param average_score: The average score of the contestant
    :return: The filtered list
    """
    i = 0
    new_list = []
    if operation == '<':
        for contestant in contestant_list:
            if mean_score(contestant) < average_score:
                new_list.append(contestant)
            i = i + 1
    elif operation == '>':
        for contestant in contestant_list:
            if mean_score(contestant) > average_score:
                new_list.append(contestant)
            i = i + 1
    else:
        for contestant in contestant_list:
            if mean_score(contestant) == average_score:
                new_list.append(contestant)
            i = i + 1

    return new_list


def sorted_list(contestant_list):
    """
    Sorts the list in decreasing order
    :param contestant_list: The list of all contestants
    :return: A list with of the average scores in decreasing order and a list with the of the contestants' original order
    """
    new_list = []
    k = []
    m = []
    i = 0
    for contestant in contestant_list:
        m.append(mean_score(contestant))
        k.append(i)
        i = i + 1
    x = i
    for i in range(0, x-1):
        for j in range(i, x):
            if m[i] < m[j]:
                m[i], m[j] = m[j], m[i]
                k[i], k[j] = k[j], k[i]

    for i in range(0, x):
        new_list.append(contestant_list[k[i]])

    return new_list, k


def split_command(command):
    """
    Splits command string into command word and parameters
    :return: The command word and its parameters
    """
    command = command.strip()
    tokens = command.split(' ', 1)
    command_word = tokens[0].strip().lower()
    command_params = tokens[1].strip() if len(tokens) == 2 else ''

    return command_word, command_params

# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities


def insert_contestant_ui(contestant_list, cmd_params):
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


def add_contestant_ui(contestant_list, cmd_params):
    tokens = cmd_params.split(' ')

    if len(tokens) != 3:
        raise ValueError('Invalid parameter count')

    contestant = create_contestant(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    add_contestant(contestant_list, contestant)
    print('Successfully added a new contestant')


def remove_contestant_ui(contestant_list, cmd_params):
    tokens = cmd_params.split(' ')
    if len(tokens) != 1 and len(tokens) != 3:
        raise ValueError('Invalid parameter count')

    if len(tokens) == 1:
        remove_contestant(contestant_list, int(tokens[0]))
    elif tokens[1] != 'to':
        raise ValueError('Wrong syntax')
    else:
        remove_multiple_contestant(contestant_list, int(tokens[0]), int(tokens[2]))
    print('Successfully set the scores to 0')


def replace_contestant_ui(contestant_list, cmd_params):
    tokens = cmd_params.split(' ')
    if len(tokens) != 4:
        raise ValueError('Invalid parameter count')

    if tokens[2] != 'with':
        raise ValueError('Wrong syntax')

    if tokens[1] != 'P1' and tokens[1] != 'P2' and tokens[1] != 'P3':
        raise ValueError('Wrong syntax')

    replace_contestant(contestant_list, int(tokens[0]), int(tokens[3]), tokens[1])
    print('Successfully modified the score')


def show_list_ui(contestant_list, cmd_params):
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


def start_command_ui():
    contestant_list = []
    test_init(contestant_list)
    command_dict = {'list': show_list_ui, 'add': add_contestant_ui, 'remove': remove_contestant_ui, 'insert': insert_contestant_ui, 'replace': replace_contestant_ui}
    done = False
    while not done:
        command = input('command: ')
        try:
            cmd_word, cmd_params = split_command(command)
            if cmd_word in command_dict:
                command_dict[cmd_word](contestant_list, cmd_params)
            elif cmd_word == 'exit':
                done = True
            else:
                print('Invalid command')
        except ValueError as ve:
            print(str(ve))


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert


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


test_create_contestant()
test_mean_score()
test_add_contestant()
test_insert_contestant()
test_remove_contestant()
test_remove_multiple_contestant()
test_replace_contestant()
test_display_list()
test_sorted_list()

start_command_ui()

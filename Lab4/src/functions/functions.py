"""
Functions that implement program features. They should call each other, or other functions from the domain
"""
from src.domain.entity import create_contestant, get_p1, get_p2, get_p3, set_p1, set_p2, set_p3


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
            set_p1(contestant, 0)
            set_p2(contestant, 0)
            set_p3(contestant, 0)
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
            set_p1(contestant, 0)
            set_p2(contestant, 0)
            set_p3(contestant, 0)
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
    for contestant in contest_list:
        if i == position:
            if problem == 'P1':
                set_p1(contestant, new_score)
            elif problem == 'P2':
                set_p2(contestant, new_score)
            else:
                set_p3(contestant, new_score)
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


def average(contestant_list, start, end):
    """
    Returns the average of the average scores in an interval
    :param contestant_list: The list of all contestants
    :param start: The position from where we start
    :param end: The position where we end
    :return: The average of the averages
    """
    i = 0
    addition = 0
    for contestant in contestant_list:
        if start <= i <= end:
            addition = addition + mean_score(contestant)
        i = i + 1
    return addition / (end-start+1)


def minimum(contestant_list, start, end):
    """
    Returns the minimum of the average scores in an interval
    :param contestant_list: The list of all contestants
    :param start: The position from where we start
    :param end: The position where we end
    :return: The minimum of the averages
    """
    i = 0
    minimum_score = 11
    for contestant in contestant_list:
        if start <= i <= end:
            if mean_score(contestant) < minimum_score:
                minimum_score = mean_score(contestant)
        i = i + 1
    return minimum_score


def top_contestants(contestant_list, number):
    """
    Creates a list ordered by the average scores
    :param contestant_list: The list of all contestants
    :param number: The number of contestants shown in the ordered list
    :return: The list
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
    for i in range(0, x - 1):
        for j in range(i, x):
            if m[i] < m[j]:
                m[i], m[j] = m[j], m[i]
                k[i], k[j] = k[j], k[i]

    for i in range(0, number):
        new_list.append(contestant_list[k[i]])

    return new_list, k, m


def top_contestants_score(contestant_list, number, problem):
    """
    Creates a list ordered by the score of a problem
    :param contestant_list: The list of all contestants
    :param number: The number of contestants displayed in the list
    :param problem: The problem used for ordering
    :return: The list
    """
    new_list = []
    k = []
    m = []
    i = 0
    for contestant in contestant_list:
        if problem == 'P1':
            m.append(get_p1(contestant))
        elif problem == 'P2':
            m.append(get_p2(contestant))
        else:
            m.append(get_p3(contestant))
        k.append(i)
        i = i + 1
    x = i
    for i in range(0, x - 1):
        for j in range(i, x):
            if m[i] < m[j]:
                m[i], m[j] = m[j], m[i]
                k[i], k[j] = k[j], k[i]

    for i in range(0, number):
        new_list.append(contestant_list[k[i]])

    return new_list, k, m


def remove_compare(contestant_list, operation, average_score):
    """
    Sets to 0 the values of all contestants following a certain criteria
    :param contestant_list: The list of all contestants
    :param operation: The operation used for filtering
    :param average_score: The average score used for comparing
    :return: -
    """
    average_score = average_score/10
    if operation == '<':
        for contestant in contestant_list:
            if mean_score(contestant) < average_score:
                set_p1(contestant, 0)
                set_p2(contestant, 0)
                set_p3(contestant, 0)
    elif operation == '>':
        for contestant in contestant_list:
            if mean_score(contestant) > average_score:
                set_p1(contestant, 0)
                set_p2(contestant, 0)
                set_p3(contestant, 0)


def undo(contestant_list, history_list):
    """
    Reverts back tot the previous list of contestants
    :param contestant_list: The list of all contestants
    :param history_list: The list of all the previous lists
    :return: The immediately previous list and the list of all the other previous lists
    """
    contestant_list = list(history_list[-1])
    history_list.pop()
    return contestant_list, history_list


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

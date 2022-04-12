"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


def create_contestant(p1, p2, p3):
    """
    Create contestant with given parameters
    :param p1: score of p1
    :param p2: score of p2
    :param p3: score of p3
    """
    if p1 < 0 or p1 > 10 or p2 < 0 or p2 > 10 or p3 < 0 or p3 > 10:
        raise ValueError('Cannot create contestant using given arguments')
    return [p1, p2, p3]


def get_p1(contestant):
    return contestant[0]


def get_p2(contestant):
    return contestant[1]


def get_p3(contestant):
    return contestant[2]


def set_p1(contestant, value):
    contestant[0] = value


def set_p2(contestant, value):
    contestant[1] = value


def set_p3(contestant, value):
    contestant[2] = value


def to_str(index, contestant):
    """
    Build the str representation for a contestant
    :param index: the index of the contestant
    :param contestant: The contestant
    :return: Its str representation
    """
    return 'Contestant number ' + str(index) + ': ' + str(get_p1(contestant)) + ' ' + str(get_p2(contestant)) + ' ' + str(get_p3(contestant))

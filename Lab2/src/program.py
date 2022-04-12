#
# Write the implementation for A2 in this file
# Contains at most 3 distinct values.
# Both real and imaginary parts can be written using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 131, 11-313i).

# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

def create_complex(real, imaginary):
    return [real, imaginary]


def get_real(z):
    return z[0]


def get_imaginary(z):
    return z[1]


def digits(z):
    """
    Checks what digits are used in a certain complex number
    :param z: the complex number
    :return: list of 0s and 1s representing the digits used
    """
    k = []
    for i in range(0, 10):
        k.append(0)
    real = abs(get_real(z))
    imaginary = abs(get_imaginary(z))
    if 0 < real < 10:
        k[real] = 1
    else:
        while real > 0:
            k[real % 10] = 1
            real = real//10
    if 0 < imaginary < 10:
        k[imaginary] = 1
    else:
        while imaginary > 0:
            k[imaginary % 10] = 1
            imaginary = imaginary//10
    return k


def three_values(position, complex_list):
    """
    Finds the index of the last element of the sequence containing at most 3 distinct value
    :param position: the index
    :param complex_list: the list of complex numbers
    :return: the index of the last element of the sequence
    """
    l1 = complex_list[position]
    position = position + 1
    l2 = []
    l3 = []
    while not l2:
        if complex_list[position] == l1:
            position = position + 1
        else:
            l2 = complex_list[position]
    while not l3:
        if complex_list[position] == l1 or complex_list[position] == l2:
            position = position + 1
        else:
            l3 = complex_list[position]
    while position < len(complex_list) and (complex_list[position] == l1 or complex_list[position] == l2 or complex_list[position] == l3):
        position = position + 1
    return position


def show_first_sequence(complex_list):
    """
    The longest sequence containing at most 3 distinct values
    :param complex_list: the list of complex numbers
    :return: the list containing the required sequence
    """
    sequence_list = complex_list
    max_count = 0
    for position in range(len(complex_list)-3):
        first_position = position
        last_position = three_values(first_position, complex_list)
        count = last_position - first_position
        if max_count < count:
            sequence_list = []
            max_count = count
            for i in range(first_position, last_position):
                sequence_list.append(complex_list[i])
    return sequence_list


def show_second_sequence(complex_list):
    """
    The longest sequence containing numbers where both the real and the imaginary part use the same digits
    :param complex_list: the list of complex numbers
    :return: the list containing the required sequence
    """
    sequence_list = [complex_list[0]]
    max_count = 1
    for position in range(len(complex_list)-1):
        count = 1
        first_position = position
        first_digits = digits(complex_list[position])
        last_position = position + 1
        while last_position < len(complex_list) and first_digits == digits(complex_list[last_position]):
            count = count + 1
            last_position = last_position + 1
        if max_count < count:
            max_count = count
            sequence_list = []
            for i in range(first_position, last_position):
                sequence_list.append(complex_list[i])

    return sequence_list


def to_str(z):
    """
    Transforms the complex number into a string
    :param z: the complex number
    :return: the display of the complex number as a string
    """
    if get_imaginary(z) > 0 and get_real(z) != 0:
        return str(get_real(z)) + '+' + str(get_imaginary(z)) + 'i'
    elif get_imaginary(z) < 0 and get_real(z) != 0:
        return str(get_real(z)) + str(get_imaginary(z)) + 'i'
    elif get_imaginary(z) == 0:
        return str(get_real(z))
    else:
        return str(get_imaginary(z)) + 'i'

# print('Hello A2'!) -> prints aren't allowed here!


# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities

def read_complex():
    real = int(input('Real part:'))
    imaginary = int(input('Read imaginary:'))
    return create_complex(real, imaginary)


def print_menu():
    print('1. Read a list')
    print('2. Show the current list')
    print('3. Display the longest sequence containing at most 3 distinct values')
    print('4. Display the longest sequence containing numbers where both the real and the imaginary part use the same digits')
    print('5. Exit application')


def read_list_ui(complex_list):
    finished = False
    print('\n')
    while not finished:
        option = input("Do you want to add a new element?")
        if option == 'Yes':
            complex_list.append(read_complex())
        elif option == 'No':
            finished = True
            print('\n')
            print('List updated!')
            print('\n')
        else:
            print('\n')
            print('Not a valid answer!')
            print('\n')
    return complex_list


def show_list_ui(complex_list):
    print('\n')
    print('The current list is: ')
    for z in complex_list:
        print(to_str(z))
    print('\n')


def show_first_sequence_ui(complex_list):
    first_sequence = show_first_sequence(complex_list)
    print('\n')
    print('The longest sequence containing at most 3 distinct values: ')
    for z in first_sequence:
        print(to_str(z))
    print('\n')


def show_second_sequence_ui(complex_list):
    second_sequence = show_second_sequence(complex_list)
    print('\n')
    print("The longest sequence containing numbers where both the real and the imaginary part use the same digits: ")
    for z in second_sequence:
        print(to_str(z))
    print('\n')


def start():
    complex_list = []
    test_init(complex_list)
    command_dict = {'1': read_list_ui, '2': show_list_ui, '3': show_first_sequence_ui, '4': show_second_sequence_ui}
    done = False
    while not done:
        print_menu()
        command = input("Enter command: ")
        if command in command_dict:
            command_dict[command](complex_list)
        elif command == '5':
            print('\n')
            print('Application closed.')
            done = True
        else:
            print('\n')
            print('Invalid command!')
            print('\n')


def test_init(complex_list):
    complex_list.append(create_complex(-13, 313))
    complex_list.append(create_complex(3, 13))
    complex_list.append(create_complex(1313, -3331))
    complex_list.append(create_complex(7, 0))
    complex_list.append(create_complex(7, -9))
    complex_list.append(create_complex(-10, 3))
    complex_list.append(create_complex(7, -9))
    complex_list.append(create_complex(7, -9))
    complex_list.append(create_complex(0, 13))
    complex_list.append(create_complex(-10, 3))


start()

class Iterator:
    def __init__(self, col):
        self._collection = col
        self._poz = 0

    def __next__(self):
        if self._poz == len(self._collection.data):
            raise StopIteration()
        self._poz += 1
        return self._collection.data[self._poz - 1]


class IterableObject:

    def __init__(self):
        self.data = []

    def __iter__(self):
        return Iterator(self)

    def add(self, elem):
        self.data.append(elem)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)


def gnome_sort(arr, arr2, sort_method):
    if not arr2:
        index = 0
        while index < len(arr):
            if index == 0:
                index = index + 1
            if sort_method(arr[index], arr[index - 1]):
                index = index + 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index = index - 1

        return arr
    else:
        index = 0
        while index < len(arr):
            if index == 0:
                index = index + 1
            if sort_method(arr[index], arr[index - 1]):
                index = index + 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                arr2[index], arr2[index - 1] = arr2[index - 1], arr2[index]
                index = index - 1

        return arr, arr2


def filter_list(given_list, condition):
    first_element = given_list[0]
    if type(first_element) == list or type(first_element) == tuple:
        number = int(input("The element for which the filter condition should be applied (starts at 0): "))
        new_list = [element for element in given_list if condition(element[number])]
        return new_list
    else:
        new_list = [element for element in given_list if condition(element)]
        return new_list


import unittest
from module import gnome_sort, filter_list, IterableObject


class TestModule(unittest.TestCase):

    def test_gnome_sort_simple(self):
        array = [67, 4, 5, 0, 1, 5, 2, 8, 10]
        gnome_sort(array, [], self.sort_method)
        self.assertEqual(array, [0, 1, 2, 4, 5, 5, 8, 10, 67])

    def test_filter(self):
        array = [67, 4, 5, 0, 1, 5, 2, 8, 10]
        pairs = [('Joanna', 6), ('Anna', 10), ('Carl', 9), ('Betty', 8), ('Xavier', 5), ('Sophia', 7), ('Richard', 7)]
        array = filter_list(array, self.condition1)
        pairs = filter_list(pairs, self.condition2)
        self.assertEqual(array, [67, 5, 5, 8, 10])
        self.assertEqual(pairs, [('Anna', 10)])

    @staticmethod
    def condition1(element):
        return element > 4

    @staticmethod
    def condition2(element):
        return element == 'Anna'

    @staticmethod
    def sort_method(a, b):
        return a >= b

    def test_gnome_sort_complex(self):
        array = [67, 4, 5, 0, 1, 5, 2, 8, 10]
        array2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        gnome_sort(array, array2, self.sort_method)
        self.assertEqual(array, [0, 1, 2, 4, 5, 5, 8, 10, 67])
        self.assertEqual(array2, ['d', 'e', 'g', 'b', 'c', 'f', 'h', 'i', 'a'])

    def test_iterable(self):

        self._test_list = IterableObject()
        self._test_list.add('Peacock')
        self._test_list.add('Plum')
        self._test_list.add('Scarlet')
        self._test_list.add('Mustard')

        for person in self._test_list:
            self.assertIn(person, ['Peacock', 'Plum', 'Scarlet', 'Mustard'])

        self.assertEqual(self._test_list[0], 'Peacock')
        self.assertEqual(self._test_list[1],  'Plum')
        self.assertEqual(self._test_list[2], 'Scarlet')
        self.assertEqual(self._test_list[3], 'Mustard')

        self._test_list[2] = 'White'
        self.assertEqual(self._test_list[2], 'White')
        self.assertEqual(self._test_list[3], 'Mustard')

        del self._test_list[0]
        del self._test_list[0]
        del self._test_list[0]

        self.assertEqual(self._test_list[0], 'Mustard')

        del self._test_list[0]
        self.assertEqual(len(self._test_list), 0)

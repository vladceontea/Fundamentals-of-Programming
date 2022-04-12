"""
    Entity class should be coded here
"""


class Book:

    def __init__(self, isbn='', title='', author=''):
        """
        Defines the Book type
        :param isbn: The ISBN code of the book
        :param title: The title of the book
        :param author: The author of the book
        """
        self._isbn = isbn
        self._title = title
        self._author = author

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @title.setter
    def title(self, value):
        self._title = value

    @author.setter
    def author(self, value):
        self._author = value

    def __str__(self):
        return '\033[36m' + 'ISBN: ' + '\033[0m' + self.isbn + '\033[36m' + ' Title: ' + '\033[0m' + self.title + '\033[36m' + ' Author: ' + '\033[0m' + self.author


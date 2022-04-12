"""
    Service class includes functionalities for implementing program features
"""

import copy
import random

from src.domain.entity import Book


class Service:

    def __init__(self):
        self.books = []
        self.history = []

    def add_book(self, book):
        """
        Adds the book to the list of all books
        :param book: The book data read from the console
        :return: -
        """
        new_list = copy.deepcopy(self.books)
        self.history.append(new_list)
        self.books.append(book)

    def add_random_book(self):
        """
        Adds a random book to the list of all books, containing data from a list
        :return: -
        """
        new_list = copy.deepcopy(self.books)
        self.history.append(new_list)
        done = False
        while not done:
            book = Book(random.choice(isbn_list), random.choice(title_list), random.choice(author_list))
            double = False
            for element in self.books:
                if book.isbn == element.isbn or book.title == element.title:
                    double = True
            if double is False:
                self.books.append(book)
                done = True

    def filter_books(self, word):
        new_list = copy.deepcopy(self.books)
        self.history.append(new_list)
        i = 0
        while i < len(self.books):
            first_word = self.books[i].title.split(' ')
            if first_word[0] == word:
                self.books.pop(i)
            else:
                i = i+1

    def undo(self):
        self.books = list(self.history[-1])
        self.history.pop()

    def __str__(self):
        for book in self.books:
            print(str(book))


isbn_list = ['978-0-1143-5752-8', '978-8-0580-1931-1', '978-1-8228-4963-3', '978-4-9091-3702-9', '978-7-3708-8495-9', '978-5-5665-9592-4', '978-6-8370-0740-5', '978-1-6209-0963-8', '978-2-3395-3601-6', '978-2-7173-8420-8', '978-7-1984-7358-8', '978-9-2190-6864-3', '978-2-1398-8216-0', '978-2-2069-7943-4', '978-0-4862-6402-8', '978-5-4977-2950-4', '978-4-1785-6555-4', '978-9-4782-9221-6', '978-8-8659-6895-6', '978-7-1713-8840-3', '978-7-6757-6745-2', '978-7-2777-5330-3', '978-8-5011-2126-4', '978-1-0733-4164-1', '978-0-1618-3222-1']
title_list = ['The Weeping Star', 'The Throne of the Trident', 'Eclipse of Ceres', 'Prince\'s Mask', 'The Solitary Wedding', 'Made of Fury', 'Resonant Light', 'Secret of the Mute Baker', 'Californian Gold', 'Sign of the Hollow Staircase', 'Plague of Blood', 'Something Gained', 'The Titan in the Sea', 'Secret of the Vanishing Man', 'Ladders of Love', 'The Town', 'Kaus', 'Cosmic Vortex', '2105: Omega', 'Queen of Capella', 'Lacy and Racy', 'The Dark Bow', 'Babylon Ascending', 'Copper Heart', 'A Man\'s Man', 'Mark of Winter', '2105: Alpha', 'Secret of the Andes']
author_list = ['Christiana Fitzpatrick', 'Sarah-Jayne Hodson', 'Lola-Mae Koch', 'Phoenix Murphy', 'Jason Mcfarlane', 'Perry Hollis', 'Jo Melia', 'Levi Mccray', 'Anna-Maria Santos', 'Aiden Norris', 'Rajan Avila', 'Justin Woods', 'Steve Ireland', 'Athena Tillman', 'Lilli O\'Neill', 'Beatrice Ahmed', 'Kennedy Barton', 'Edmund Fry', 'Mandy Stott', 'Giulia Alvarez', 'Terrence Carver', 'Sabrina Burris', 'Hannah Berry', 'Connor Harwood', 'Taliah Gale']


def test_add_random_book():
    my_list = Service()
    for i in range(10):
        my_list.add_random_book()
    assert len(my_list.books) == 10


def test_add_book():
    my_list = Service()
    b1 = Book('978-7-9876-5432-0', 'The Forgotten Lands', 'Lewis Fox')
    b2 = Book('978-4-6277-5012-1', 'The Sands of Time', 'Katy Woods')
    my_list.add_book(b1)
    my_list.add_book(b2)
    assert len(my_list.books) == 2


test_add_random_book()
test_add_book()

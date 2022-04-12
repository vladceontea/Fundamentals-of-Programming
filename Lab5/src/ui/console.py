"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from src.domain.entity import Book
from src.services.service import Service


class UI:

    def __init__(self, book_list):
        self._commands = {'1': self.add_book, '2': self.show_books, '3': self.filter_books, '4': self.undo}
        self._books = book_list

    @staticmethod
    def _print_menu():
        print('1. Add a book')
        print('2. Show all books')
        print('3. Filter the list of books')
        print('4. Undo the last operation')
        print('5. Exit')

    def add_book(self):
        isbn = input("Add the isbn code of the book (978-x-xxxx-xxxx-x) : ")
        if int(isbn[0]) != 9 or int(isbn[1]) != 7 or int(isbn[2]) != 8 or isbn[3] != '-' or isbn[5] != '-' or isbn[10] != '-' or isbn[15] != '-':
            raise ValueError("Not a valid code")
        title = input("Add the title of the book: ")
        author = input("Add the author of the book: ")
        b = Book(isbn, title, author)
        double = False
        for element in self._books.books:
            if b.isbn == element.isbn or b.title == element.title:
                print("The book already exists!")
        if double is False:
            self._books.add_book(b)

    def show_books(self):
        for book in self._books.books:
            print(str(book))

    def filter_books(self):
        word = input("Give a word: ")
        self._books.filter_books(word)

    def undo(self):
        done = False
        answer = 'Yes'
        while done is False:
            if len(self._books.history) == 0:
                raise ValueError('No operations to undo!')
            elif answer == 'Yes':
                self._books.undo()
                print("Undid last operation")
            answer = input("Do you want to undo another operation? ")
            if answer == 'No':
                done = True
            elif answer != 'Yes' and answer != 'No':
                print("Not a valid answer")

    def start(self):
        self.test_init()
        self._books.history = []
        while True:
            self._print_menu()
            _command = input("Enter command: ")
            try:
                if _command == '5':
                    print('Exited application')
                    return
                if _command not in self._commands:
                    print('Invalid command!')
                else:
                    self._commands[_command]()
            except ValueError as ve:
                print(str(ve))

    def test_init(self):
        for i in range(10):
            self._books.add_random_book()

from src.domain.entity import Book
from src.services.service import Service
from src.ui.console import UI

books = Service()

ui = UI(books)

ui.start()

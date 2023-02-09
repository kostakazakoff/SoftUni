class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book, location):
        self.books.update({book: location})

    def find_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book

    def __repr__(self):
        return '\n'.join(f'{book.title}: {book.author}, location -> {location}' for book, location in self.books.items())


# book1 = Book('Alabala1', 'Alabala1')
# book2 = Book('Alabala2', 'Alabala2')
# library = Library()
# library.add_book(book1, 'A1')
# library.add_book(book2, 'B2')
# print(library)
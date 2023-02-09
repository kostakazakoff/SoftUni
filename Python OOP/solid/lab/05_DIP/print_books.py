class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter()):
        formatted_book = formatter.format(book)
        return formatted_book


# class HTMLFormatter:
#     @staticmethod
#     def format(book: Book) -> str:
#         book.content = f'<html>{book.content}<\html>'
#         return book.content

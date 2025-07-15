from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content

class SimpleFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:10]


class InstagramFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:5]


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter) -> str:
        formatted_book = formatter.format(book)
        return formatted_book


b = Book("Hi there! How are you?")

f = PaperFormatter()
p = Printer()
print(p.get_book(b, f))
class Book:
    def __init__(self, title, author, pages=0):
        self.title = title
        self.author = author
        self.page = pages

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f'Title: {self.title} ({self.page} pages) with author: {self.author}'


class Library:
    def __init__(self, books: list[Book]):
        self.books = books

    def find_book_by_title(self, title: str) -> Book | str:
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return "We do not have this book"

    def find_book_by_author(self, author: str) -> Book | str:
        try:
            book = [b for b in self.books if b.author == author][0]
            return book
        except IndexError:
            return "We do not have this author"

    def add_book(self, book: Book):
        self.books.append(book)

    def delete_book(self, book: Book):
        pass


b1 = Book("To kill a mocking bird", "Author", 400)
b2 = Book("Harry Potter 5", "J. Austin", 800)
b3 = Book("Test", "Test", 20)

library = Library([b1, b2, b3])

print(library.find_book_by_title("asd"))
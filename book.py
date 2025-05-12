#!/usr/bin/python3
"""Book and EBook class definition with inheritance and encapsulation."""


class Book:
    """A class representing a physical book."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  # Encapsulated attribute

    def description(self):
        """Return a short description of the book."""
        return f"'{self.title}' by {self.author}, {self._pages} pages."

    def read(self):
        """Simulate reading the book."""
        return "📖 You're reading a physical book."


class EBook(Book):
    """A subclass representing an electronic book."""

    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # In megabytes

    def read(self):
        """Override the read method to simulate e-reading."""
        return "💻 You're reading on an e-reader."


if __name__ == "__main__":
    my_book = Book("1984", "George Orwell", 328)
    my_ebook = EBook("Digital Fortress", "Dan Brown", 384, 1.2)

    print(my_book.description())
    print(my_book.read())
    print(my_ebook.description())
    print(my_ebook.read())

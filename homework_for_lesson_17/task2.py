# Write a class structure that implements a library. Classes:

# 1) Library - name, books = [], authors = []

# 2) Book - name, year, author (author must be an instance of Author class)

# 3) Author - name, country, birthday, books = []

# Library class

# Methods:

# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

# - group_by_author(author: Author) - returns a list of all books grouped by the specified author

# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.

# Also, the book class should have a class variable which holds the amount of all existing books



class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]
    
    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books}, authors={self.authors})"

    def __str__(self):
        book_names = []
        for book in self.books:
            book_names.append(book.name)
        author_names = []
        for author in self.authors:
            author_names.append(author.name)
        return f"Library: {self.name}\nBooks: {', '.join(book_names)}\nAuthors: {', '.join(author_names)}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author})"

    def __str__(self):
        return f"Book: {self.name} ({self.year}) by {self.author.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}', books={self.books})"

    def __str__(self):
        return f"Author: {self.name} from {self.country}, born {self.birthday}, he has written {self.books}"

book1 = Book("The Fearsome World of Dinosaurs", 2023, "Some dinosaur")
library1 = Library("Dinosaurarium")
author1 = Author("Some dinosaur", "There were no continents back then really", "80 million years ago")
author1.add_book("The Fearsome World of Dinosaurs")
print(author1)
library1.new_book("The Fearsome World of Dinosaurs", "80million years ago", "Some dinosaur")
 #Obligatorisk opgave 1 - Library Management System

# We want to create a simple library management system.

# 1. First we define the classes, these are blueprints that define our data structure

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        

class Member:
    def __init__(self, member_id, name, borrowed_books):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books
        self.return_book = self.return_book

class Library:
    def __init__(self, books, members):
        self.books = books
        self.members = members
        
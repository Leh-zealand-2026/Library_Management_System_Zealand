 #Obligatorisk opgave 1 - Library Management System

# We want to create a simple library management system.

# 1. First we define the classes, these are blueprints that define our data structure

# self allows us to establish a variable in one function and use it in another

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
    # Defining method, these are functions that are tied to an object
    # In this case it's simply print functions to show book information
    def display_info(self):
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")  
        print(f"Author: {self.author}")  
        print(f"Copies: {self.copies}")   
        
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = [] # Create list to keep track of a members borrowed books
    
    # We need methods for borrowing and returning books

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id) # This method adds a book to our members borrowed_books list
    
    def return_book(self, book_id):
        if book_id in self.borrowed_books: # Check the members own borrowed_books list
            self.borrowed_books.remove(book_id) # If the ID matches then remove from list
        else:
            print("Book not found.")

    def display_info(self):
        print(f"ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Borrowed Books: {self.borrowed_books}")

# The library keeps track of books and members, these are saved as objects in lists.
class Library:
    def __init__(self):
        self.books = {} # List of books
        self.members = {} # List of members
    
    def add_book(self, book):
        self.books[book.book_id] = book # We add the book objects

    def add_member(self, member):
        self.members[member.member_id] = member # adding member object


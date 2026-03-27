# Pytest file 

# Pytest checks for any files named test to open and inside those files
# it checks for any functions named test to test, so thats why we need to begin with test_


# We create a test_ function for every function that we have created in our main file

from main import Book, Member, Library

# Testing our add book function in library()

def test_add_book():
    lib = Library()
    # Set the values of our book object
    book = Book("2026", "Harry Potter", "JK Rowling", 10)

    lib.add_book(book)

    # Check if the book ID 2026 matches any book in our database
    assert "2026" in lib.books

# Test for adding members

def test_add_member():
    lib = Library()
    # Set values of our member
    member = Member("23", "Lebron James")

    lib.add_member(member)

    # Check if any member id matches who we just added
    assert "23" in lib.members

def test_issue_book():
    lib = Library()
    book = Book("2026", "Harry Potter", "JK Rowling", 10)
    member = Member("23", "Lebron James")

    lib.add_book(book)
    lib.add_member(member)

    # Check member first then book id
    lib.issue_book("23", "2026")

    # We had 10 books, issued 1, so we expect there to be 9 books left if we issued correctly.
    assert book.copies == 9
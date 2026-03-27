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

def test_return_book():
    lib = Library()
    book = Book("2026", "Harry Potter", "JK Rowling", 1)
    member = Member("23", "Lebron James")

    lib.add_book(book)
    lib.add_member(member)

    lib.issue_book("23", "2026")
    lib.return_book("23", "2026")

    assert book.copies == 1

def test_remove_member():
    lib = Library()
    member = Member("23", "Lebron James")
    lib.add_member(member)
    lib.remove_member("23")
    assert "23" not in lib.members

# Adding some edge cases

    # We try adding 0 copies of book to library database, we then assert if
    # A. There are no copies and B. The member did not borrow copy that did not exist.
def test_issue_book_no_copy():
    lib = Library()
    book = Book("2026", "Harry Potter", "JK Rowling", 0)
    member = Member("23", "Lebron James")
    lib.add_book(book)
    lib.add_member(member)

    lib.issue_book("23", "2026")

    assert book.copies == 0
    assert member.borrowed_books == []

 # What happens if a member returns a book they didn't lend?
 # Assert that number of copies available did not change
 # Assert that member does not have a copy in his file. (Or negative or some other unusual behavious, it should be empty.)
def test_return_book_not_borrowed():
    lib = Library()
    book = Book("2026", "Harry Potter", "JK Rowling", 1)
    member = Member("23", "Lebron James")
    lib.add_book(book)
    lib.add_member(member)

    lib.return_book("23", "2026")

    assert book.copies == 1
    assert member.borrowed_books == []


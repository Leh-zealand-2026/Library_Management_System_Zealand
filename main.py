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

    # Our logic for issuing books
    def issue_book(self, member_id, book_id):


        # Checking for book_id match in the books list and handling exception
        if book_id not in self.books:
            print("No book matches that ID in the database")
            return
        
        # Checking member_id in members list
        if member_id not in self.members:
            print("Member does not exist.")
            return
        
        book = self.books[book_id]
        member = self.members[member_id]
        
        # if book and member exist we then check if copies are available
        if book.copies > 0:
            book.copies -= 1
            member.borrow_book(book_id)
            print(f"Book issued successfully to {member_id}")
        else:
            print("No copies are currently available, please try again later")

    # Our logic for returning books is similar issueing
    def return_book(self, member_id, book_id):

        # First check if book and member exist in database
        if book_id not in self.books:
            print("Book ID match not found in database")
            return
        if member_id not in self.members:
            print("Member ID not found in database")
            return
        
        book = self.books[book_id]
        member = self.members[member_id]

        # Now we check the members list of borrowed books and update their list.
        if book_id in member.borrowed_books:
            book.copies += 1
            member.return_book(book_id)
            print(f"{book_id} was returned successfully.")
        else:
            print(f"Book was not found in {member_id}'s borrowed list.")
        
        # check for book_id match in library and removes if found
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"{book_id} removed from library.")
        else:
            print(f"{book_id} does not match any id in library.")

        # updating book, check for book_id then overwrite with new information

    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id not in self.books:
            print(f"{book_id} not found")
            return
    
        book = self.books[book_id]

        if title:
            book.title = title
        if author:
            book.author = author
        if copies is not None:
            book.copies = copies
    
        print(f"{book_id} updated.")

    # checks if books are in library and then uses display info for all books
    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        
        for book in self.books.values():
            book.display_info()
            print("_____" * 5)

    # Check for member_id match and deletes if found
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print(f"{member_id} removed from database.")
        else:
            print("No matching id found in database.")

    # Check for member_id match and updates name if found
    def update_member(self, member_id, name=None):
        if member_id not in self.members:
            print("No matching id found in database.")
            return
        
        member = self.members[member_id]

        if name:
            member.name = name
            print("Member name updated")
    
    # check for members in library and then displays info for all found
    def display_members(self):
        if not self.members:
            print("No members are registered in library database")
            return
    
    for member in self.members.values():
        member.display_info()
        print("_____" * 5)


# Creating a main function that acts as our main menu and allows user to call the methods we made earlier.

def main():
    library = Library()
    
    # Our menu options
    while True:
        print("Main Menu")
        print("_____" * 5)
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Exit")

        # read user input and save as variable "choice"
        choice = input("Press the number corresponding to the action you want to perform.")

        # We use if and elif statements to check if "choice" input matches our menu options
        if choice == "1":
            print("You have chosen 'Add Book' please enter the required information\n")
            book_id = input("Enter book ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            copies = int(input("Enter number of copies: "))

            book = Book(book_id, title, author, copies)
            library.add_book(book)

        # elif checks if the previous statement was true, if not then it will check this one.
        # We use the same logic for all of our menu options
        elif choice == "2":
            print("You have chosen 'Add member'\n")
            member_id = input("Enter member ID: ")
            name = input("Enter name: ")

            member = Member(member_id, name)
            library.add_member(member)

        elif choice == "3":
            print("You have chosen 'Issue Book'\n")
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")

            library.issue_book(member_id, book_id)

        elif choice == "4":
            print("You have chosen 'Return Book'\n")
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")

            library.return_book(member_id, book_id)

        elif choice == "5":
            print("You have chosen 'Display Books'\n")    
            library.display_books()

        elif choice == "6":
            print("You have chosen 'Display Members'\n")
            library.display_members()

        elif choice == "7":
            print("You have chosen 'Exit'\n")
            break
        
        # Incase someone writes something other than our menu options we can handle it with an else statement.
        else:
            print("Invalid input, please use number corresponding to menu options.")

    # When you import python functions they are ran automatically, so to make sure we don't run code we don't intend to
    # we can use the if __name__ == "__main__" line so that main() is only run when we cal it directly
    if __name__ == "__main__":
        main()
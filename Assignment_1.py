"""
Experiment 1: Introduction to OOP Concepts
Library Management System - Menu Driven Version
"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is already borrowed")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def __str__(self):
        return f"Patron: {self.name} (ID: {self.patron_id})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Added book: {book.title}")

    def register_patron(self, name, patron_id):
        patron = Patron(name, patron_id)
        self.patrons.append(patron)
        print(f"Registered patron: {patron.name}")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    def borrow_book(self, patron_id, isbn):
        patron = self.find_patron(patron_id)
        book = self.find_book(isbn)
        if not patron:
            print("Patron not found")
            return
        if not book:
            print("Book not found")
            return
        patron.borrow_book(book)

    def return_book(self, patron_id, isbn):
        patron = self.find_patron(patron_id)
        book = self.find_book(isbn)
        if not patron:
            print("Patron not found")
            return
        if not book:
            print("Book not found")
            return
        patron.return_book(book)

    def display_books(self):
        print(f"\n--- Books in {self.name} ---")
        if not self.books:
            print("No books in the library yet.")
        for book in self.books:
            print(book)

    def display_patrons(self):
        print(f"\n--- Registered Patrons in {self.name} ---")
        if not self.patrons:
            print("No patrons registered yet.")
        for patron in self.patrons:
            print(patron)
            if patron.borrowed_books:
                titles = ", ".join(b.title for b in patron.borrowed_books)
                print(f"   Currently borrowed: {titles}")

# om kutwal sy-12 roll no. 70
def print_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add a new book")
    print("2. Register a new patron")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Display all books")
    print("6. Display all patrons")
    print("7. Exit")
    print("======================================")


def main():
    library = Library("City Central Library")

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            library.add_book(title, author, isbn)

        elif choice == "2":
            name = input("Enter patron name: ").strip()
            patron_id = input("Enter patron ID: ").strip()
            library.register_patron(name, patron_id)

        elif choice == "3":
            patron_id = input("Enter patron ID: ").strip()
            isbn = input("Enter book ISBN to borrow: ").strip()
            library.borrow_book(patron_id, isbn)

        elif choice == "4":
            patron_id = input("Enter patron ID: ").strip()
            isbn = input("Enter book ISBN to return: ").strip()
            library.return_book(patron_id, isbn)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            library.display_patrons()

        elif choice == "7":
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

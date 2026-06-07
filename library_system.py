class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class BookUnavailableError(LibraryError):
    pass

class LoanNotFoundError(LibraryError):
    pass


class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.book_id}] {self.title} - {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __str__(self):
        return f"[{self.member_id}] {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = {}

    def add_book(self, book_id, title):
        self.books[book_id] = Book(book_id, title)
        print("Book added successfully.")

    def add_member(self, member_id, name):
        self.members[member_id] = Member(member_id, name)
        print("Member added successfully.")

    def borrow_book(self, book_id, member_id):
        if book_id not in self.books:
            raise BookNotFoundError("Book not found.")

        if member_id not in self.members:
            raise MemberNotFoundError("Member not found.")

        book = self.books[book_id]

        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")

        book.available = False
        self.loans[book_id] = member_id
        print(f"{self.members[member_id].name} borrowed '{book.title}'")

    def return_book(self, book_id):
        if book_id not in self.loans:
            raise LoanNotFoundError("Loan record not found.")

        book = self.books[book_id]
        book.available = True
        del self.loans[book_id]
        print(f"Book '{book.title}' returned successfully.")

    def show_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            print(book)

    def show_members(self):
        if not self.members:
            print("No members found.")
            return
        for member in self.members.values():
            print(member)

    def show_loans(self):
        if not self.loans:
            print("No active loans.")
            return
        for book_id, member_id in self.loans.items():
            print(f"Book '{self.books[book_id].title}' is borrowed by {self.members[member_id].name}")


def main():
    library = Library()

    while True:
        print("\n=== Library System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Books")
        print("6. Show Members")
        print("7. Show Loans")
        print("0. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                book_id = input("Enter Book ID: ")
                title = input("Enter Book Title: ")
                library.add_book(book_id, title)

            elif choice == "2":
                member_id = input("Enter Member ID: ")
                name = input("Enter Member Name: ")
                library.add_member(member_id, name)

            elif choice == "3":
                book_id = input("Enter Book ID: ")
                member_id = input("Enter Member ID: ")
                library.borrow_book(book_id, member_id)

            elif choice == "4":
                book_id = input("Enter Book ID: ")
                library.return_book(book_id)

            elif choice == "5":
                library.show_books()

            elif choice == "6":
                library.show_members()

            elif choice == "7":
                library.show_loans()

            elif choice == "0":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Try again.")

        except LibraryError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
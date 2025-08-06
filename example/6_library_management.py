"""
Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you can print all books, 
add a book and get the number of books using different methods. Show that your program doesn’t persist the books after the program is stopped!
"""


class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f"Book '{book_name}' added successfully.")

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

    def get_number_of_books(self):
        print(f"Total number of books: {self.no_of_books}")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Get Number of Books")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            library.get_number_of_books()
        elif choice == '4':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

  

      




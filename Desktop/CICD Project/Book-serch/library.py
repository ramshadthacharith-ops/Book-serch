import json

FILE_NAME = "books.json"


def load_books():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def display_books(books):
    print("\nLibrary Books")
    print("-" * 60)

    for book in books:
        status = "Available" if book["available"] else "Borrowed"

        print(f"""
ID        : {book['id']}
Title     : {book['title']}
Author    : {book['author']}
Category  : {book['category']}
Status    : {status}
""")


def search_title(books):
    keyword = input("Enter title: ").lower()

    found = False

    for book in books:
        if keyword in book["title"].lower():
            print(book)
            found = True

    if not found:
        print("Book not found.")


def search_author(books):
    keyword = input("Enter author: ").lower()

    found = False

    for book in books:
        if keyword in book["author"].lower():
            print(book)
            found = True

    if not found:
        print("Book not found.")


def search_category(books):
    keyword = input("Enter category: ").lower()

    found = False

    for book in books:
        if keyword in book["category"].lower():
            print(book)
            found = True

    if not found:
        print("Book not found.")


def borrow_book(books):
    book_id = int(input("Enter Book ID: "))

    for book in books:
        if book["id"] == book_id:

            if book["available"]:
                book["available"] = False
                save_books(books)
                print("Book borrowed successfully.")
            else:
                print("Book already borrowed.")

            return

    print("Book ID not found.")


def return_book(books):
    book_id = int(input("Enter Book ID: "))

    for book in books:

        if book["id"] == book_id:

            if not book["available"]:
                book["available"] = True
                save_books(books)
                print("Book returned successfully.")
            else:
                print("Book is already available.")

            return

    print("Book ID not found.")


def main():

    while True:

        books = load_books()

        print("""
======== Library Management ========

1. Display Books
2. Search by Title
3. Search by Author
4. Search by Category
5. Borrow Book
6. Return Book
7. Exit

====================================
""")

        choice = input("Choose: ")

        if choice == "1":
            display_books(books)

        elif choice == "2":
            search_title(books)

        elif choice == "3":
            search_author(books)

        elif choice == "4":
            search_category(books)

        elif choice == "5":
            borrow_book(books)

        elif choice == "6":
            return_book(books)

        elif choice == "7":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
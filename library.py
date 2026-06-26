import json

FILE_NAME = "books.json"


def load_books():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def search_book():
    books = load_books()

    keyword = input("Enter book name: ").lower()
    found = False

    print("\n📚 Search Results\n" + "-" * 40)

    for book in books:
        if keyword in book["title"].lower():

            status = "Available" if book["available"] else "Borrowed"

            print(f"""
ID        : {book['id']}
Title     : {book['title']}
Author    : {book['author']}
Category  : {book['category']}
Status    : {status}
""")
            found = True

    if not found:
        print("❌ Book not found")


def main():
    while True:
        print("""
===== Library System =====

1. Search Book
2. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            search_book()

        elif choice == "2":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

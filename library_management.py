# Library Management System
# MBIS402 Project (Basic but solid version)

books = []

def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")
    print("=====================================")

def add_book():
    book = input("Enter book name: ").strip()
    if book:
        books.append(book)
        print(f"'{book}' added successfully!")
    else:
        print("Book name cannot be empty.")

def view_books():
    if not books:
        print("No books available.")
    else:
        print("\n--- Book List ---")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")

def search_book():
    keyword = input("Enter book name to search: ").strip().lower()
    found = False

    for book in books:
        if keyword in book.lower():
            print(f"Found: {book}")
            found = True

    if not found:
        print("Book not found.")

def remove_book():
    view_books()
    try:
        index = int(input("Enter book number to remove: "))
        if 1 <= index <= len(books):
            removed = books.pop(index - 1)
            print(f"'{removed}' removed successfully!")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()

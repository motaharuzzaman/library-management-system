import save_all_books
from datetime import datetime

def lend_book(all_books):
    search_book = input("Enter Book Title to lend: ")
    for book in all_books:
        if book["title"] == search_book:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                book["bookLastUpdatedAt"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                save_all_books.save_all_books(all_books)
                print(f"Book '{book['title']}' lent successfully.")
                return all_books
            else:
                print("No book is available to lend.")
                return all_books

    print("Book Not Found")
    return all_books


def return_book(all_books):
    search_book = input("Enter Book Title to Return: ")
    for book in all_books:
        if book["title"] == search_book:
            book["quantity"] += 1
            book["bookLastUpdatedAt"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            save_all_books.save_all_books(all_books)
            print(f"Book '{book['title']}' returned successfully.")
            return all_books

    print("Book Not Found")
    return all_books

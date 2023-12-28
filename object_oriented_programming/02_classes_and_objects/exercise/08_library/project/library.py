from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}
        self.rented_books: Dict[str, Dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            if user not in self.user_records:
                self.user_records.append(user)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username].update({book_name: days_to_return})
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for b in self.rented_books.values():
            if book_name in b:
                days = b[book_name]
                return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        if author not in self.books_available:
            self.books_available[author] = []
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]




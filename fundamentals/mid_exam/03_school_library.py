def adding(book, collection):
    if book not in collection:
        collection.insert(0, book)
    return collection


def removing(book, collection):
    if book in collection:
        collection.remove(book)
    return collection


def swapping(book_one, book_two, collection):
    if book_one in collection and book_two in collection:
        book_one_index = collection.index(book_one)
        book_two_index = collection.index(book_two)
        collection[book_two_index], collection[book_one_index] = collection[book_one_index], collection[book_two_index]
    return collection


def inserting(book, collection):
    if book not in collection:
        collection.append(book)
    return collection


def checking(book_index, collection):
    if book_index <= len(collection):
        print(f'{collection[book_index]}')
    return False


shelf_with_books = input().split("&")
command = input()

while command != "Done":
    command = command.split(" | ")
    action = command[0]
    if action == "Add Book":
        current_book = command[1]
        shelf_with_books = adding(current_book, shelf_with_books)
    elif action == "Take Book":
        current_book = command[1]
        shelf_with_books = removing(current_book, shelf_with_books)
    elif action == "Swap Books":
        current_book1 = command[1]
        current_book2 = command[2]
        shelf_with_books = swapping(current_book1, current_book2, shelf_with_books)
    elif action == "Insert Book":
        current_book = command[1]
        shelf_with_books = inserting(current_book, shelf_with_books)
    elif action == "Check Book":
        book_place = int(command[1])
        checking(book_place, shelf_with_books)
    command = input()
print(*shelf_with_books, sep=", ")


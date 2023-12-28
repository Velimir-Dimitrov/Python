book = input()
count_check = 0

while True:
    book_check = input()
    if book == book_check:
        print(f"You checked {count_check} books and found it.")
        break
    if book_check == "No More Books":
        print(f"The book you search is not here!\nYou checked {count_check} books.")
        break
    count_check += 1
try:
    with open("01_text.txt", 'a') as f:
        print("File found")
except FileNotFoundError:
    print("File not found")


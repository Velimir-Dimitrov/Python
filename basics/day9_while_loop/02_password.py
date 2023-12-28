user = input()
current_password = input()

while True:
    password = input()
    if current_password == password:
        print(f"Welcome {user}!")
        break
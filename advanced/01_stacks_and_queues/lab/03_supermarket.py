from collections import deque
clients = deque()

while True:
    command = input()
    if command == "Paid":
        while clients:
            print(clients.popleft())
    elif command == "End":
        print(f"{len(clients)} people remaining.")
        break
    else:
        clients.append(command)

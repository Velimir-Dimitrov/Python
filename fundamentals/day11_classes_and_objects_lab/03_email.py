class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails = []

while command != "Stop":
    tokens = command.split(" ")
    sender, receiver, content = tokens[0], tokens[1], tokens[2]
    current_email = Email(sender, receiver, content)
    emails.append(current_email)
    command = input()

indices = [int(el) for el in input().split(",")]
for index, email in enumerate(emails):
    if index in indices:
        Email.send(email)
    print(Email.get_info(email))

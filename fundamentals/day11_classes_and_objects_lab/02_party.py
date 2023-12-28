class Party:
    def __init__(self):
        self.people = []


name = input()
party = Party()

while name != "End":
    party.people.append(name)
    name = input()

print(f"Going: {', '.join(party.people)}\nTotal: {len(party.people)}")
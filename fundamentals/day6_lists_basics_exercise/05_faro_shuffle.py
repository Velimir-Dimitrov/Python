current_deck = input().split(" ")
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_deck = []
    mid_split = len(current_deck) // 2
    left_side_deck = current_deck[0:mid_split]
    right_side_deck = current_deck[mid_split:]
    for index in range(mid_split):
        final_deck.append(left_side_deck[index])
        final_deck.append(right_side_deck[index])
        current_deck = final_deck
print(current_deck)

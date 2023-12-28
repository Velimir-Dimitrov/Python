tickets = input().split(", ")
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()
    match_symbol = ""
    uninterrupted_match_length = 0
    second_match = 0
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    for first_half_index in range(10):
        if ticket[first_half_index] in winning_symbols:
            match_symbol = ticket[first_half_index]
            for index1 in range(first_half_index, 10):
                if ticket[index1] != match_symbol:
                    break
                uninterrupted_match_length += 1
            break
    for second_half_index in range(10,20):
        if ticket[second_half_index] == match_symbol:
            for index2 in range(second_half_index, 20):
                if ticket[index2] != match_symbol:
                    break
                second_match += 1
            break
    if uninterrupted_match_length > second_match:
        uninterrupted_match_length = second_match
    if uninterrupted_match_length >= 10:
        print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!')
        continue
    elif 6 <= uninterrupted_match_length:
        print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
        continue

    else:
        print(f'ticket "{ticket}" - no match')


# def check_ticket(ticket):
#     if len(ticket) != 20:
#         return "invalid ticket"
#     winning_symbols = ['@', '#', '$', '^']
#     left_part = ticket[:10]
#     right_part = ticket[10:]
#     for match_symbol in winning_symbols:
#         for uninterrupted_match_length in range(10, 5, -1):
#             winning_symbols_repetition = match_symbol * uninterrupted_match_length
#             if winning_symbols_repetition in left_part and winning_symbols_repetition in right_part:
#                 if uninterrupted_match_length == 10:
#                     return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
#                 return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
#     return f'ticket "{ticket}" - no match'
# 
#
# tickets = [ticket.strip() for ticket in input().split(", ")]
# for ticket in tickets:
#     print(check_ticket(ticket))

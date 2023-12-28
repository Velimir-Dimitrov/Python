import math
magnolia = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
present_cost = float(input())

earned = magnolia * 3.25 + hyacinths * 4 + roses * 3.50 + cacti * 8
taxes = (earned * 5) / 100
after_tax = earned - taxes

diff = abs(present_cost - after_tax)

if present_cost <= after_tax:
    print(f'She is left with {math.floor(diff)} leva.')
elif present_cost > after_tax:
    print(f'She will have to borrow {math.ceil(diff)} leva.')
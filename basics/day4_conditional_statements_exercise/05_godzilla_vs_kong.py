movie_budget = float(input())
number_extras = int(input())
cost_per_extra = float(input())

cost_of_decor = movie_budget * 0.1
cost_of_extras = number_extras * cost_per_extra

if number_extras > 150:
    cost_of_extras *= 0.9

movie_cost = cost_of_extras + cost_of_decor
diff = abs(movie_budget - movie_cost)

if movie_cost > movie_budget:
    print("Not enough money!")
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print("Action!")
    print(f'Wingard starts filming with {diff:.2f} leva left.')


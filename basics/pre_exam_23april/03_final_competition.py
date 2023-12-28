number_dancers = int(input())
points = float(input())
season = input()
place = input()

reward = 0

if place == "Bulgaria":
    reward = points * number_dancers
elif place == "Abroad":
    reward = (points * number_dancers) * 1.5

if place == "Bulgaria" and season == "summer":
    reward *= 0.95
elif place == "Bulgaria" and season == "winter":
    reward *= 0.92
elif place == "Abroad" and season == "summer":
    reward *= 0.90
elif place == "Abroad" and season == "winter":
    reward *= 0.85

charity_sum = reward * 0.75
reward_per_dancer = (reward - charity_sum) / number_dancers

print(f'Charity - {charity_sum:.2f}')
print(f"Money per dancer - {reward_per_dancer:.2f}")
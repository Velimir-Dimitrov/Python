actor_name = input()
points = float(input())
number_reviewers = int(input())

max_points = 1250.5

for reviewer in range(number_reviewers):
    reviewer_name = input()
    rating = float(input())
    points += (len(reviewer_name) * rating) / 2
    if points >= max_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
else:
    needed_points = max_points - points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")


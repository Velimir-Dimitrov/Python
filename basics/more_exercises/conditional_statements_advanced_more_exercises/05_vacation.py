budget = float(input())
season = input()

if budget <= 1000 and season == "Summer":
    budget *= 0.65
    print(f"Alaska - Camp - {budget:.2f}")
elif 1000 < budget <= 3000 and season == "Summer":
    budget *= 0.8
    print(f"Alaska - Hut - {budget:.2f}")
elif budget <= 1000 and season == "Winter":
    budget *= 0.45
    print(f"Morocco - Camp - {budget:.2f}")
elif 1000 < budget <= 3000 and season == "Winter":
    budget *= 0.6
    print(f"Morocco - Hut - {budget:.2f}")
elif budget > 3000:
    budget *= 0.9
    if season == "Summer":
        print(f"Alaska - Hotel - {budget:.2f}")
    elif season == "Winter":
        print(f"Morocco - Hotel - {budget:.2f}")
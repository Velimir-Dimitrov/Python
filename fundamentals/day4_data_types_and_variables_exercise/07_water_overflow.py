n = int(input())
capacity = 255
water_poured = 0

for i in range(n):
    water = int(input())
    if (capacity - water) >= 0:
        water_poured += water
        capacity -= water
    else:
        print("Insufficient capacity!")
print(water_poured)
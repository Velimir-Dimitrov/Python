total_load = int(input())

total_tons = 0
total_price = 0
bus = 0
truck = 0
train = 0

for _ in range(1, total_load + 1):
    tons_per_load = int(input())
    total_tons += tons_per_load
    if tons_per_load <= 3:
        bus += tons_per_load
        total_price += tons_per_load * 200
    elif tons_per_load <= 11:
        truck += tons_per_load
        total_price += tons_per_load * 175
    else:
        train += tons_per_load
        total_price += tons_per_load * 120
bus_percentage = bus / total_tons * 100
truck_percentage = truck / total_tons * 100
train_percentage = train / total_tons * 100
average_price = total_price / total_tons
print(f'{average_price:.2f}')
print(f'{bus_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')
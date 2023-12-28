days = int(input())

total_litres = 0
total_degrees = 0

for day in range(1, days + 1):
    litres_per_day = float(input())
    degrees_per_day = float(input())
    total_litres += litres_per_day
    total_degrees += litres_per_day * degrees_per_day

average_degrees = total_degrees / total_litres

print(f"Liter: {total_litres:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees < 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
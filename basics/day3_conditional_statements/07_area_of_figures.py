figure = input()
area = 0

if figure == "square":
    side = float(input())
    area = side * side
if figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
if figure == "circle":
    radius = float(input())
    from math import pi
    area = pi * (radius **2)
if figure == "triangle":
    base_side = float(input())
    height_side = float(input())
    area = base_side * height_side * 0.5

print(f'{area:.3f}')
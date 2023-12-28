house_height = float(input())
house_length = float(input())
roof_height = float(input())

house_side_area = house_length * house_height
window_area = 1.5 * 1.5
real_side_house_area = 2 * house_side_area - 2 * window_area

house_front_area = house_height * house_height
door_area = 1.2 * 2
real_front_house_area = 2 * house_front_area - door_area

real_house_area = real_front_house_area + real_side_house_area
green_paint = real_house_area / 3.4


roof_side_area = 2 * (house_height * house_length)
roof_front_area = 2 * (house_height * roof_height / 2)
total_roof_area = roof_front_area + roof_side_area
red_paint = total_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')



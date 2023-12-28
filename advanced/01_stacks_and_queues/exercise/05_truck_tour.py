from collections import deque
number_of_pumps = int(input())
pumps = deque()

for pump_number in range(number_of_pumps):
    current_line = [int(x) for x in input().split()]
    pumps.append(current_line)


for pump in range(number_of_pumps):
    tour_pump = False
    tank_fuel = 0
    distance = 0
    for stop in range(number_of_pumps):
        tank_fuel += pumps[stop][0]
        distance += pumps[stop][1]
        if tank_fuel < distance:
            pumps.rotate(-1)
            tour_pump = False
            break
        tour_pump = True
    if tour_pump:
        print(pump)
        break


# from collections import deque
#
# petrol_pumps = int(input())
#
# pumps = deque()
# for _ in range(petrol_pumps):
#     pump_info = [int(x) for x in input().split()]
#     pumps.append(pump_info)
#
#
# for attempt in range(petrol_pumps):
#     tank = 0
#     full_circle = True
#     for fuel, distance in pumps:
#         tank += fuel
#         if distance > tank:
#             full_circle = False
#             break
#         else:
#             tank -= distance
#     if full_circle:
#         print(attempt)
#         break
#     else:
#         pumps.append(pumps.popleft())
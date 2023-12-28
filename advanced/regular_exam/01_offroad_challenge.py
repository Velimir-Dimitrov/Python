from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption = deque(int(x) for x in input().split())
required_fuel = deque(int(x) for x in input().split())
SEQUENCE_LEN = 4
REACHED_ALL = False
reached_altitudes = []


while True:
    current_fuel = initial_fuel.pop()
    current_additional_consumption = additional_consumption.popleft()
    current_fuel_result = current_fuel - current_additional_consumption
    current_required_fuel = required_fuel.popleft()
    current_altitude = SEQUENCE_LEN - len(required_fuel)
    if current_fuel_result >= current_required_fuel:
        reached_altitudes.append(current_altitude)
        print(f"John has reached: Altitude {current_altitude}")
        REACHED_ALL = True
    else:
        print(f"John did not reach: Altitude {current_altitude}")
        REACHED_ALL = False
        break

if REACHED_ALL:
    print("John has reached all the altitudes and managed to reach the top!")
elif not REACHED_ALL and 1 <= len(reached_altitudes):
    print("John failed to reach the top.")
    print(f"Reached altitudes: Altitude {', Altitude '.join(str(altitude) for altitude in reached_altitudes)}")
else:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")





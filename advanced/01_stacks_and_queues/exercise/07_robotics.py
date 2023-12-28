from collections import deque

robots_data = input().split(";")
robots = []
for robot_data in robots_data:
    robot_name, robot_time = robot_data.split("-")
    robots.append({"name": robot_name, "time": [int(robot_time), 0]})

current_time = [int(x) for x in input().split(":")]
hours, minutes, seconds = current_time
starting_time = hours * 3600 + minutes * 60 + seconds

products = deque()
command = input()
while command != "End":
    products.append(command)
    command = input()

while products:
    current_product = products.popleft()
    starting_time += 1
    is_taken = False
    for robot in robots:
        if robot["time"][1] <= starting_time:
            robot["time"][1] = starting_time + robot["time"][0]
            is_taken = True
            h = starting_time // 3600
            m = (starting_time % 3600) // 60
            s = (starting_time % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            break
    if not is_taken:
        products.append(current_product)


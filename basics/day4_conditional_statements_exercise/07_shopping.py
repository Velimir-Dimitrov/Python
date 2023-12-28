budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())

total_gpu_price = number_gpu * 250
cpu_price_per_one = total_gpu_price * 0.35
total_cpu_price = cpu_price_per_one * number_cpu
ram_price_per_one = total_gpu_price * 0.10
total_ram_price = ram_price_per_one * number_ram

total_price = total_ram_price + total_cpu_price + total_gpu_price

if number_gpu > number_cpu:
    total_price *= 0.85

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
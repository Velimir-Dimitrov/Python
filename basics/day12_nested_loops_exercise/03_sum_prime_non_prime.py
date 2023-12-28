import math
total_prime = 0
total_non_prime = 0
prime_flag= False
while True:
      command = input()
      if command == "stop":
            break
      number = int(command)
      if number < 0:
            print("Number is negative.")
            continue
      for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                 prime_flag = True
                 break
            else:
                  prime_flag = False
      if prime_flag:
            total_non_prime += number
      else:
            total_prime += number
print(f'Sum of all prime numbers is: {total_prime}')
print(f"Sum of all non prime numbers is: {total_non_prime}")








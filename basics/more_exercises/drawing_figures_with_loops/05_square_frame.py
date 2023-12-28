n = int(input())
dash = " -"
print(f'+{dash * (n - 2)} +')
for col in range(0, n-2):
    print(f'|{dash * (n -2)} |')
print(f'+{dash * (n - 2)} +')
import re
line_command = input()
pattern = r"%([A-Z][a-z]+)%[^\.\%\$\|]*<(\w+)>[^\.\%\$\|]*\|(\d+)\|[^\.\%\$\|\[0-9]*([0]|[1-9][0-9]*\.?[0-9]*)\$"
income = 0

while line_command != "end of shift":
    valid_order = re.findall(pattern, line_command)
    if valid_order:
        customer_name, product, quantity, price = valid_order[0]
        total_price = int(quantity) * float(price)
        income += total_price
        print(f"{customer_name}: {product} - {total_price:.2f}")
    line_command = input()
print(f"Total income: {income:.2f}")


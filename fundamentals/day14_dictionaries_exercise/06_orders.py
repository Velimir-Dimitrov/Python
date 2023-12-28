products_dict = {}
while True:
    entry = input()
    if entry == "buy":
        break
    product_name, price, quantity = entry.split(" ")
    price = float(price)
    quantity = int(quantity)
    if product_name not in products_dict.keys():
        products_dict[product_name] = [price, quantity]
    else:
        products_dict[product_name][0] = price
        products_dict[product_name][1] += quantity
for product, price_and_quantity in products_dict.items():
    total_price = price_and_quantity[0] * price_and_quantity[1]
    print(f"{product} -> {total_price:.2f}")



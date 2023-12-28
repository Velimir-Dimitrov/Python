def grocery_store(**kwargs):
    result = ""
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x)))
    for product_name, product_quantity in sorted_dict.items():
        result += f'{product_name}: {product_quantity}\n'
    return result


print(grocery_store(bread=5, pasta=12, eggs=12,))
print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1,))


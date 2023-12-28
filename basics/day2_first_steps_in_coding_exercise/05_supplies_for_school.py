packages_of_pens = int(input()) * 5.80
packages_of_markers = int(input()) * 7.20
litres_of_cleaner = int(input()) * 1.20
discount = int(input()) /100
all_products = packages_of_pens + packages_of_markers + litres_of_cleaner
price_with_discount = all_products - (all_products * discount)
print(price_with_discount)

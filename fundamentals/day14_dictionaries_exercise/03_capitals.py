countries = input().split(", ")
cities = input().split(", ")

[(print(f"{country} -> {city}")) for country, city in zip(countries, cities)]


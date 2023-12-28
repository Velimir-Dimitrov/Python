import re
years = input()
valid_filter = r"\b(?P<Day>\d{2})(?P<sep>\/|.|-)(?P<Month>[A-Z][a-z][a-z])(?P=sep)(?P<Year>\d{4})\b"
valid_years = re.finditer(valid_filter, years)
for year in valid_years:
    year = year.groupdict()
    print(f"Day: {year['Day']}, Month: {year['Month']}, Year: {year['Year']}")
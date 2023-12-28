command = input()
companies_dict = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies_dict:
        companies_dict[company_name] = []
    if employee_id not in companies_dict[company_name]:
        companies_dict[company_name].append(employee_id)
    command = input()

for company_name, employees in companies_dict.items():
    print(company_name)
    for employee_id in companies_dict[company_name]:
        print(f"-- {employee_id}")
company_info = {}

while True:
    line = input()

    if line == "End":
        break



    company, employee_id = line.split(" -> ")

    if company not in company_info:
        company_info[company] = []

    if employee_id not in company_info[company]:
        company_info[company].append(employee_id)

for company, users in company_info.items():
    print(company)
    for employee_id in users:
        print(f"-- {employee_id}")


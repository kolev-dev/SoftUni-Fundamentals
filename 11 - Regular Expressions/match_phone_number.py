import re

phone_numbers = input()

match = re.findall(r'\+359 \d \d{3} \d{4}|\+359-\d-\d{3}-\d{4}$', phone_numbers)
print(", ".join(match))

import re

phone_numbers = input()

match = re.findall(r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b', phone_numbers)
print(", ".join(match))


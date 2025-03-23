import re

total_points = 0
valid_destinations = []


destinations = input()

pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, destinations)

for match in matches:
    destination = match[1]
    valid_destinations.append(destination)
    total_points += len(destination)

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {total_points}")






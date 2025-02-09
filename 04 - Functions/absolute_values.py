number_sequence = input().split()


numbers_with_absolute_values = []

def absolute_value(value):
    return abs(float(value))

for number in number_sequence:
    numbers_with_absolute_values.append(absolute_value(number))

print(numbers_with_absolute_values)


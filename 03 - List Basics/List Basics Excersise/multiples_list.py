factor = int(input())
count = int(input())

numbers_list = []

for number in range(1, count +1):
    current_value = number * factor
    numbers_list.append(current_value)

print(numbers_list)
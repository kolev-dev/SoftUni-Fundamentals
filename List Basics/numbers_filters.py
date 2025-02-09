n = int(input())

unfiltered_numbers = []
filtered_numbers = []

for _ in range(n):
    num = int(input())
    unfiltered_numbers.append(num)

command = input()

if command == "even":
    for number in unfiltered_numbers:
        if number % 2 == 0 or number == 0:
            filtered_numbers.append(number)


elif command == "odd":
    for number in unfiltered_numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)

elif command == "negative":
    for number in unfiltered_numbers:
        if number < 0:
            filtered_numbers.append(number)


elif command == "positive":
    for number in unfiltered_numbers:
        if number >= 0:
            filtered_numbers.append(number)


print(filtered_numbers)
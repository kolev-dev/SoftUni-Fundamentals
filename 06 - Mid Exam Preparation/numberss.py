numbers = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "Finish":
        break

    elif command[0] == "Add":
        numbers.append(int(command[1]))

    elif command[0] == "Remove":
        numbers.remove(int(command[1]))

    elif command[0] == "Replace":
        if int(command[1]) in numbers:
            index_found = numbers.index(int(command[1]))
            numbers[index_found] = int(command[2])

    elif command[0] == "Collapse":
        # for index, num in enumerate(numbers):
        #     if num <= int(command[1]):
        #         numbers.pop(index)
        # for number in numbers:
        #     if number < int(command[1]):
        #         numbers.remove(number)
        numbers = [num for num in numbers if num >= int(command[1])]

numbers_as_str = list(map(str, numbers))
print(" ".join(numbers_as_str))


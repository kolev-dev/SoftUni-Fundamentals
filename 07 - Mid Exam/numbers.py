numbers = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "Finish":
        break

    elif command[0] == "Add":
        numbers.append(int(command[1]))

    elif command[0] == "Remove":
        index_found = numbers.index(int(command[1]))
        numbers.pop(index_found)

    elif command[0] == "Replace":
        if command[1] in numbers:
            index_found = numbers.index(int(command[1]))
            numbers[index_found] = int(command[2])

    elif command[0] == "Collapse":
        for index, num in enumerate(numbers):
            if num < int(command[1]):
                numbers.pop(index)


numbers_as_str = list(map(str, numbers))
print(" ".join(numbers_as_str))


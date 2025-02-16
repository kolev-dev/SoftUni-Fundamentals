def operations_and_prints(numbers_sequence: list, group: int):
    current_group_list = [num for num in numbers_sequence if num <= group]
    print(f"Group of {group}'s: {current_group_list}")

    for number in current_group_list:
        numbers_sequence.remove(number)





numbers = list(map(int, input().split(", ")))

group = 10
while numbers:

    threshold = max(numbers)

    if threshold > group:
        operations_and_prints(numbers,group)
        group += 10
    else:
        operations_and_prints(numbers, group)
        break
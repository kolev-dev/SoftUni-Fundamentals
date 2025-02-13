numbers_sequence = list(map(int, input().split(", ")))

indexes_of_even_numbers = [index for index, element in enumerate(numbers_sequence) if element % 2 == 0]
print(indexes_of_even_numbers)



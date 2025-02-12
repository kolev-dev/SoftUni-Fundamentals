numbers_sequence = list(map(int, input().split(", ")))

# even_indexes = [numbers_sequence.index(number) for number in numbers_sequence if number % 2 == 0]


even_indexes = []
for number in numbers_sequence:
    if number % 2 == 0:
        current_index = numbers_sequence.index(number)
        even_indexes.append(current_index)

print(even_indexes)

#needs rework (failed one check at judge)
def filter_even(n):
    return n % 2 == 0



numbers_sequence = map(int, input().split())
filtered_sequence = list(filter(filter_even, numbers_sequence))
print(filtered_sequence)
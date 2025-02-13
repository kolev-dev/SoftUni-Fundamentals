numbers_sequence = list(map(int, input().split()))

filtered = [number for number in numbers_sequence if number > sum(numbers_sequence) / len(numbers_sequence)]



descending_order = sorted(filtered, reverse=True)
descending_order_strings = list(map(str, descending_order))

for n in range(5):
    print(descending_order_strings[n])

# print(" ".join(descending_order_strings))




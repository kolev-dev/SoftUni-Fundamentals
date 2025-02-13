numbers_sequence = list(map(int, input().split()))

filtered =[]
count = 0

for number in numbers_sequence:
    count += 1
    if number > sum(numbers_sequence) / len(numbers_sequence):
            filtered.append(number)

descending_order = sorted(filtered, reverse=True)
descending_order_strings = list(map(str, descending_order))

print(" ".join(descending_order_strings))

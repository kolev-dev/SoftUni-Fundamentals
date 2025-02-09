elements_list = input().split()
faro_shuffles = int(input())


left_part = []
right_part = []

for shuffle in range(faro_shuffles):
    left_part = elements_list[: len(elements_list) // 2]
    right_part = elements_list[len(elements_list) // 2:]

    final_shuffle = []
    for index in range(len(elements_list) // 2):
        final_shuffle.append(left_part[index])
        final_shuffle.append(right_part[index])
    elements_list = final_shuffle.copy()

print(final_shuffle)
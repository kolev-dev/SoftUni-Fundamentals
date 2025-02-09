numbers_list = input().split(", ")
beggars_count = int(input())

beggars_sums = []
current_beggar_sum = 0
start_index = 0


for current_beggar in range(beggars_count):
    current_beggar_sum = 0
    for current_index in range(start_index, len(numbers_list), beggars_count):
        current_beggar_sum += int(numbers_list[current_index])

    beggars_sums.append(current_beggar_sum)
    start_index +=1

print(beggars_sums)



# in this loop we get the index of the value of which the current_bagger is
# for beggar_indexes in range(1, len(numbers_list), beggars_count):
#     current_sum += int(numbers_list[beggar_indexes])
#     beggars_sums.append(current_sum)



# for beggar in range(beggars_count):
#     for number in 1, numbers_list, beggars_count:
#         print(number)
#         current_sum += int(number)
#         beggars_sums.append(current_sum)


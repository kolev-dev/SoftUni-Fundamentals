input_list = input().split()

opposite_list = list()


for current_number in input_list:
    opposite_number = -int(current_number)
    opposite_list.append(opposite_number)

print(opposite_list)
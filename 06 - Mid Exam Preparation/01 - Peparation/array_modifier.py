# def decrease_with_1(n):
#     return n - 1
#
# You can use map in line 26 instead of list comprehension with this func

my_array = list(map(int, input().split()))

while True:
    command = input().split()


    if command[0] == "end":
        break

    if command[0] == "swap":
        my_array[int(command[1])], my_array[int(command[2])] = my_array[int(command[2])], my_array[int(command[1])]

    elif command[0] == "multiply":
        element_in_list1 = my_array[int(command[1])]
        element_in_list2 = my_array[int(command[2])]


        my_array[int(command[1])] = int(element_in_list1) * int(element_in_list2)

    elif command[0] == "decrease":
        my_array = [int(n) - 1 for n in my_array]


list_as_strings = list(map(str, my_array))
print(", ".join(list_as_strings))
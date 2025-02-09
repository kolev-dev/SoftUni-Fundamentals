list_of_integers = input().split()
n = int(input())

elements_to_remove = []

sorted_list = []
for element in list_of_integers:
    sorted_list.append(int(element))

sorted_list.sort()

#remove from sorting
for _ in range(n):
    pop_value = sorted_list.pop(0)
    elements_to_remove.append(pop_value)


for element_removal in elements_to_remove:
    list_of_integers.remove(str(element_removal))




print(", ".join(list_of_integers))

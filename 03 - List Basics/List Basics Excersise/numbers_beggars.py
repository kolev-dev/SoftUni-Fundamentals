numbers = list(map(int, input().split(", ")))
count_of_beggars = int(input())

beggars = []
start_index = 0

for beggar in range(count_of_beggars):
    beggars_sum = 0
    for index_number in range(start_index, len(numbers), count_of_beggars):
        beggars_sum += numbers[index_number]


    beggars.append(beggars_sum)
    start_index += 1

print(beggars)
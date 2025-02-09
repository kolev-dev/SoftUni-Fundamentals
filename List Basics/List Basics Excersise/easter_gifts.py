gifts = input().split()

while True:
    command = input().split()


    if command[0] == 'No' and command[1] == 'Money':
        break

    if command[0] == 'OutOfStock':
        if command[1] in gifts:

            # current_gift_count_in_list = gifts.count(command[1])

            if gifts.count(command[1]) < 1:
                index_found = gifts.index(command[1])
                gifts[index_found] = "None"
            else:
                # for gift_index in range(current_gift_count_in_list):
                #     gifts.remove(command[1])


                # we use the len of gifts cuz we want to get the index of the element and work with it!
                for gift_index in range(len(gifts)):
                    if gifts[gift_index] == command[1]:
                        gifts[gift_index] = "None"


    elif command[0] == 'Required':
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]



    elif command[0] == 'JustInCase':
        gifts.pop()
        gifts.append(command[1])


# Want to remove every "None" from gifts
while "None" in gifts:
    gifts.remove("None")


print(' '.join(gifts))


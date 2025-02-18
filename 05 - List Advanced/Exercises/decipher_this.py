# secret_words = input().split()
#
# for word in secret_words:
#
#     value_of_index_1 = word[1]
#     value_of_last_index = word[-1]
#
#     word = word.raplce(value_of_last_index,value_of_index_1)
#
#     # word = word.replace(word[0], chr(int(word[0])))
#     print(word)

secret_words = input().split()


# for word in secret_words:
#     number = []
#
#     for string in word:
#         if string.isdigit():
#             number.append(string)
#
#         else:

# sliceing
counter = 0
break_flag = False

for word in secret_words:
    if break_flag:
        continue
    for string in word:
        if string.isdigit():
            counter +=1
        else:
            break_flag = True
            continue

    word_number = word[:counter]
    word_strings = word[counter:]







    print(f"{chr(int(word_number))}{word_strings}")
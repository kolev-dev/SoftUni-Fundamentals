words = input().split(" ")

words_as_dict = {}

for word in words:

    word = word.lower()

    if word not in words_as_dict:
        words_as_dict[word] = 1

    else:
        words_as_dict[word] += 1

for key, value in words_as_dict.items():
    if value % 2 != 0:
        print(key, end = " ")
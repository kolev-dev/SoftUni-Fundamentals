sequence_of_words = input().split(", ")
second_sequence = input().split(", ")

filtered_sequence = [word for word in sequence_of_words if any(word in word2 for word2 in second_sequence)]
print(filtered_sequence)



words = input().split()

new_words = [word * len(word) for word in words]

print("".join(new_words))
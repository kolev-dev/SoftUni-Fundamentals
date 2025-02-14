words = input().split()

filtered_even_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_even_words))
letters = input().split(", ")

letter_values = {}

for letter in letters:
    letter_values[letter] = ord(letter)

print(letter_values)
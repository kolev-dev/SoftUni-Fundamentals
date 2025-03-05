text = input()
characters = {}

for char in text:
    if char == " ":
        continue
    if char not in characters.keys():
        characters[char] = 0
    characters[char] += 1

for character, count in characters.items():
    print(f"{character} -> {count}")
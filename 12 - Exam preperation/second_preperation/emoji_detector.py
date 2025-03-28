import re

text = input()

cool_threshold = 1

digits_pattern = r"\d"
matched_digits = re.findall(digits_pattern, text)
for digit in matched_digits:
    cool_threshold *= int(digit)

# emojis_pattern = r"\s(\*\*|::)([A-Z][a-z]{2,})\1"
emoji_pattern = re.compile(r'(\*\*[A-Z][a-z]{2,}\*\*|::[A-Z][a-z]{2,}::)')
matched_emojis = emoji_pattern.findall(text)
# print(matched_emojis)


print(f"Cool threshold: {cool_threshold}")
print(f"{len(matched_emojis)} emojis found in the text. The cool ones are:")

# for symbols, word in matched_emojis:
#     emoji_coolness = sum(ord(char) for char in word)
#     if emoji_coolness > cool_threshold:
#         print(f"{symbols}{word}{symbols}")

for emoji in matched_emojis:
    emoji_coolness = sum(ord(char) for char in emoji[2:-2])
    if emoji_coolness > cool_threshold:
        print(emoji)

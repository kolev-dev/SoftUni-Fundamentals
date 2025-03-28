import re

text = input()

pattern = r"([@|#])([A-za-z]{2,})\1\1([A-Za-z]{3,})\1"
pair_words = re.findall(pattern, text)

matched_words =[]

for word in pair_words:
    if word[1] == word[2][::-1]:
        matched_words.append(f"{word[1]} <=> {word[2]}")

if not pair_words:
    print("No word pairs found!")
    if matched_words:
        print("The mirror words are: ")
        print(", ".join(matched_words))
    else:
        print("No mirror words!")
else:
    print(f"{len(pair_words)} word pairs found!")
    if matched_words:
        print("The mirror words are: ")
        print(", ".join(matched_words))
    else:
        print("No mirror words!")
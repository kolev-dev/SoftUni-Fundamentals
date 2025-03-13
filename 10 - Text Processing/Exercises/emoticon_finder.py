text = input()

emoticons = []

for index in range(len(text)):
    if text[index] == ":":
        if index + 1 < len(text):
            emoticons.append(f":{text[index + 1]}")

for emoticon in emoticons:
    print(emoticon)

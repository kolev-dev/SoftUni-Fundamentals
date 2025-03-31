import re

n = int(input())
patter = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'
valid_messages = []


for i in range(1, n + 1):
    text = input()
    matches = re.findall(patter, text)
    valid_messages.append(matches)


for match in valid_messages:
    if not match:
        print("The message is invalid")

    for tup in match:
        command, message  = tup

        translated_letters = [str(ord(letter)) for letter in message]
        print(f"{command}: {' '.join(translated_letters)}")

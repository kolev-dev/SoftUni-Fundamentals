text = input()

while True:
    command = input().split()

    action = command[0]

    if action == "End":
        break

    if action == "Translate":
        char, replacement = command[1:]
        text = text.replace(char, replacement)
        print(text)

    elif action == "Includes":
        substring = command[1]
        if substring in text:
            print(True)
        else:
            print(False)

    elif action == "Start":
        substring = command[1]
        if text.startswith(f'{substring}'):
            print(True)
        else:
            print(False)

    elif action == "Lowercase":
        text = text.lower()
        print(text)

    elif action == "FindIndex":
        char = command[1]
        print(text.rindex(char))

    elif action == "Remove":
        start_index, count = command[1:]

        substring_to_remove = text[int(start_index): int(count) + int(start_index)]
        text = text.replace(substring_to_remove, "")
        print(text)
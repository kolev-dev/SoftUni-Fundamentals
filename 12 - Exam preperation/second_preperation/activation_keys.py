raw_key = input()

while True:
    command = input().split(">>>")
    action = command[0]

    if action == 'Generate':
        break

    if action == 'Contains':
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == 'Flip':
        selected_case = command[1] # is ether Upper or Lower
        start_index = int(command[2])
        end_index = int(command[3])

        substring = raw_key[start_index:end_index]

        if selected_case == 'Upper':
            substring_case = substring.upper()
        elif selected_case == 'Lower':
            substring_case = substring.lower()

        # raw_key[start_index:end_index] = substring_case
        raw_key = raw_key.replace(substring, substring_case)
        print(raw_key)

    elif action == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        substring = raw_key[start_index:end_index]
        raw_key = raw_key.replace(substring, "")
        print(raw_key)

print(f"Your activation key is: {raw_key}")

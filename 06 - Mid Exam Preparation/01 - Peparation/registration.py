def change_letters(lst):
    if lst[1] == "Lower":
        return username.lower()

    elif lst[1] == "Upper":
        return username.lower()


def reverse_letters(lst):
    text = username[int(lst[1]):int(lst[2]) + 1]
    reversed_text = text[::-1]
    return reversed_text

def subtracting(lst):
    if lst[1] in username:
        return username.replace(lst[1],"")
    else:
        return f"The username john doesn't contain {lst[1]}."

def replacing(lst):
    if lst[1] in username:
        # username.index(lst[1])
        new_username = username.replace(lst[1],"-")
        return new_username

def isvalid(lst):
    if lst[1] in username:
        return "Valid username."
    else:
        return f"{lst[1]} must be contained in your username."




username = input()

while True:
    command = input().split()

    if command[0] == "Registration":
        break

    if command[0] == "Letters":
        print(change_letters(command))

    elif command[0] == "Reverse":
        print(reverse_letters(command))

    elif command[0] == "Substring":
        print(subtracting(command))

    elif command[0] == "Replace":
        username = replacing(command)
        print(username)

    elif command[0] == "IsValid":
        print(isvalid(command))
first_string = input()
second_string = input()

if first_string in second_string:
    second_string = second_string.replace(first_string, "")

print(second_string)
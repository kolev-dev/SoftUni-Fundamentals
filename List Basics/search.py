n = int(input())
word = input()

unfiltered_strings = []
filtered_strings = []

for i in range(n):
    string = input()

    unfiltered_strings.append(string)

    if word in string:
        filtered_strings.append(string)


print(unfiltered_strings)
print(filtered_strings)


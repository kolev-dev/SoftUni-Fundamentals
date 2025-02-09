coffee_needed = 0

while True:
    word = input()

    if word == "END":
        break

    if word.lower() == "coding" \
        or word.lower() == "dog"\
        or word.lower() == "cat"\
        or word.lower() == "movie":

        if word.islower():
            coffee_needed += 1

        if word.isupper():
            coffee_needed += 2

    else:
        pass

if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
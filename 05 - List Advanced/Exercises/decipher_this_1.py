message = input()

deciphered_message = []

for word in message.split():
    first_letter_acii = ""

    for letter in word:
        if letter.isdigit():
            first_letter_acii += letter
            word = word.replace(letter, "")

    if not len(word) < 2:
        new_word = word[-1] + word[1:-1] + word[0]
    else:
        new_word = word[0]

    deciphered_message.append(f"{chr(int(first_letter_acii))}{new_word}")


print(" ".join(deciphered_message))
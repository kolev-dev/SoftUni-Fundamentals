repeating_letters = input()

last_letter = ""
final_letters = ""

for letter in repeating_letters:
    if letter != last_letter:
        final_letters += letter
    last_letter = letter
    
print(final_letters)
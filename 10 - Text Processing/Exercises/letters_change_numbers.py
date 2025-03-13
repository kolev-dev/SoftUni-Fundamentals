parts = input().split()
total_sum = 0


for part in parts:
    first_letter = part[0]

    before_last_number = len(part) - 1
    number = int(part[1:before_last_number])

    last_letter = part[-1]

    # letter_position = ord(first_letter) - 64
    # second_position = ord(last_letter) - 64

    if first_letter.isupper():

        number /= ord(first_letter) - 64
    else:
        number *= ord(first_letter) - 96

    if last_letter.isupper():
        number -= ord(last_letter) - 64
    else:
        number += ord(last_letter) - 96

    total_sum += number

print(f"{total_sum:.2f}")

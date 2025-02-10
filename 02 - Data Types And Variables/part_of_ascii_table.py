first_dec = int(input())
last_dec = int(input())

for current_symbol in range(first_dec, last_dec + 1):
    print(chr(current_symbol), end = " ")
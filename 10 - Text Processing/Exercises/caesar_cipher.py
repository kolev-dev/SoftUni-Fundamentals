text = input()

decrypted_text = ""

for character in text:
    order_num = ord(character)

    decrypted_text += chr(order_num + 3)

print(decrypted_text)
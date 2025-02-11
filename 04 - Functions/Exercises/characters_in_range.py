def generate_chars(first_char: str, second_char: str) -> str:
    char_list = []

    for dec in range(ord(first_char) + 1, ord(second_char)):
        char_list.append(chr(dec))

    return " ".join(char_list)

first_char = input()
second_char  = input()
print(generate_chars(first_char,second_char))
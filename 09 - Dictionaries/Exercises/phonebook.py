phone_book = {}

while True:
    line = input()

    if "-" not in line:
        line = int(line)
        break

    name, phone_number = line.split("-")

    phone_book[name] = phone_number


for _ in range(line):
    name_to_search = input()
    if name_to_search in phone_book.keys():
        print(f"{name_to_search} -> {phone_book[name_to_search]}")
    else:
        print(f"Contact {name_to_search} does not exist.")
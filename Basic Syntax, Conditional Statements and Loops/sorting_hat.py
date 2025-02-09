len_counter = 0

while True:
    name = input()

    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    for ch in name:
        len_counter += 1

    if len_counter < 5:
        print(f"{name} goes to Gryffindor.")

    elif len_counter == 5:
        print(f"{name} goes to Slytherin.")

    elif len_counter == 6:
        print(f"{name} goes to Ravenclaw.")

    elif len_counter > 6 :
        print(f"{name} goes to Hufflepuff.")

    len_counter = 0

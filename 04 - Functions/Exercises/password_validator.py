from string import digits


def password_validator(password: str) -> str:

    digits = 0
    password_invalid = False

    if 6 <= len(password) <= 10:
        pass
    else:
        password_invalid = True
        print("Password must be between 6 and 10 characters")

    # alphanumeric characters
    if password.isalnum():
        pass
    else:
        password_invalid = True
        print("Password must consist only of letters and digits")

    for element in password:
        if element.isdigit():
            digits +=1

        if digits == 2:
            break

    if digits < 2:
        password_invalid = True
        print("Password must have at least 2 digits")

    if not password_invalid:
        print("Password is valid")


password_input = input()
password_validator(password_input)







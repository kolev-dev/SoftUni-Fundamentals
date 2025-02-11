def is_palindrome(number: str):
        if str(number) == str(number[::-1]):
            return True
        else:
            return False




numbers_sequence = input().split(", ")
for element in numbers_sequence:
    print(is_palindrome(element))


def calculate_single_factorial(number: int):
    if number == 1:
        return 1
    else:
        return number * calculate_single_factorial(number-1)


def calculate_result(number1: int, number2: int):
    return calculate_single_factorial(number1) / calculate_single_factorial(number2)


first_number = int(input())
second_number = int(input())
print(f"{calculate_result(number1=first_number,number2=second_number):.2f}")


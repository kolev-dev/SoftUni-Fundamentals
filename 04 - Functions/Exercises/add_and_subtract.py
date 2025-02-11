def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2

def subtract(result: int, num3: int) -> int:
    return result - num3

def add_and_subtract(num1, num2, num3) -> int:
    final_result = sum_numbers(num1,num2)
    return subtract(final_result, num3)


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))

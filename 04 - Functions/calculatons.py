def calculator(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2



input_operator = input()
first_number = int(input())
second_number = int(input())
print(calculator(input_operator, first_number, second_number))
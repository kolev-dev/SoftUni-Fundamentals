def calculate(numbers: list) -> str:
    return f"The minimum number is {min(numbers)}\n"\
            f"The maximum number is {max(numbers)}\n"\
            f"The sum number is: {sum(numbers)}"


numbers_sequence = map(int, input().split())
print(calculate(list(numbers_sequence)))
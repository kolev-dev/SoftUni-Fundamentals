def positive_numbers(lst:list) -> str:
    return ", ".join([number for number in lst if int(number) >= 0])
def negative_numbers(lst:list) -> str:
    return ", ".join([number for number in lst if int(number) < 0])

def even_numbers(lst:list) -> str:
    return ", ".join([number for number in lst if int(number) % 2 == 0])

def odd_numbers(lst:list) -> str:
    return ", ".join([number for number in lst if int(number) % 2 != 0])



numbers_sequence = [number for number in input().split(", ")]

print(f"Positive: {positive_numbers(numbers_sequence)}")
print(f"Negative: {negative_numbers(numbers_sequence)}")
print(f"Even: {even_numbers(numbers_sequence)}")
print(f"Odd: {odd_numbers(numbers_sequence)}")


def calculate_sums(numbers_str: str) -> str:

    sum_of_odd_numbers = 0
    sum_of_even_numbers = 0

    for element in number:
        if int(element) % 2 == 0:
            sum_of_even_numbers += int(element)
        else:
            sum_of_odd_numbers += int(element)

    return f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}"


number = input()
print(calculate_sums(number))
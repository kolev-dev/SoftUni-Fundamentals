def check_perfect_number(number: int) -> str:

    perfect_sum = 0

    for current_number in range(1, number):
        if number % current_number == 0:
            perfect_sum += current_number

    if number == perfect_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(check_perfect_number(num))
def check_true(number):
    if int(number) % 2 == 0:
        return True
    return False

numbers_sequence = input().split()

filter(check_true, numbers_sequence)
print(numbers_sequence)
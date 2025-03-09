import math

number = int(input())
to_count = int(input()) # 0 or 1

# binary_repr = ""

counter = 0

while number > 0:

    leftover = number % 2


    if leftover == to_count:
        counter += 1

    number //= 2

print(counter)
divisor = int(input())
boundary  = int(input())


# Largest integer n
for n in range(boundary, divisor, -1):
    if n > 0:
        if n % divisor == 0:
            print(n)
            break

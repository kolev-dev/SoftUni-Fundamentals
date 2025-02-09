def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)

# Convert filter object to a list
print(list(b))  
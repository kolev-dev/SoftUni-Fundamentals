n = int(input())

total_sum = 0

for i in range(n):
    current_symbol = input()
    total_sum += ord(current_symbol)

print(f"The sum equals: {total_sum}")
numbers = list(map(int, input().split(", ")))

zeros = numbers.count(0)

for number in numbers:
    if 0 not in numbers:
        break
    numbers.remove(0)


zeros_lst = zeros * [0]

print(numbers + zeros_lst)
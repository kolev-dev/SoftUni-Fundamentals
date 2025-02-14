def sorting(numbers: list):
    sorted_numbers = []

    avg = sum(numbers) / len(numbers)
    for i, num in enumerate(numbers):
        if num > avg:
            if i < 5:
                sorted_numbers.append(str(num))

    return " ".join(sorted_numbers)




numbers = sorted(map(int,input().split()), reverse=True)

if numbers[0] == 1 and len(numbers) == 1:
    print("No")
else:
    print(sorting(numbers))





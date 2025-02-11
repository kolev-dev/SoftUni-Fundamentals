def find_smallest(numbers: list) -> int:
    return min(numbers)


first_num = int(input())
second_num = int(input())
third_num = int(input())
numbers = [first_num,second_num,third_num]

print(find_smallest(numbers))

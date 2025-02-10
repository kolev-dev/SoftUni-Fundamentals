from math import ceil

total_people = int(input())
elevator_capacity = int(input())

elevator_courses = total_people / elevator_capacity
print(ceil(elevator_courses))


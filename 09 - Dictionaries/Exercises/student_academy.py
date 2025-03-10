n = int(input())

grades_record = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in grades_record.keys():
        grades_record[name] = []
    grades_record[name].append(grade)


for name, grades in grades_record.items():
    avg_grade = sum(grades_record[name]) / len(grades_record[name])

    if avg_grade >= 4.50:
        print(f"{name} -> {avg_grade:.2f}")

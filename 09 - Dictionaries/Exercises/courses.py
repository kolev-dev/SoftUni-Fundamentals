taken_courses = {}

while True:
    student_info = input()

    if student_info == "end":
        break


    course, student = student_info.split(" : ")

    if course not in taken_courses:
        taken_courses[course] = []
    taken_courses[course].append(student)

for course, students in taken_courses.items():
    print(f"{course}: {len(students)}")
    # judge don't accept the following line
    # print(f"-- {'\n-- '.join(students)}")
    for student in students:
        print(f"-- {student}")



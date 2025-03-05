students = []
course_to_search = ""
corresponding_to_course = []

while True:
    info = input()

    if ":" not in info:
        course_to_search = info
        break

    else:
        name, ID, course = info.split(":")
        students.append({"name": name, "ID": ID, "course": course})


#filling list with the responding to search students
for dictionary in students:
    if course_to_search.startswith(dictionary["course"][0:3]):
        corresponding_to_course.append(dictionary)


#unpacking the list filled with the searched course
for any_student in corresponding_to_course:
    print(f"{any_student['name']} - {any_student['ID']}")
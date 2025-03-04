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


for dictionary in students:
    if course_to_search.startswith(dictionary["course"][0:3]):
        corresponding_to_course.append(dictionary)

# for responding in course_to_search:
#     print(f"{responding["name"]} - {responding[ID]}")


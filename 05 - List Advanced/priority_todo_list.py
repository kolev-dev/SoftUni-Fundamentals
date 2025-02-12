notes = []
while True:
    todo = input()

    if todo == "End":
        break

    notes.append(todo)

sorted_notes = sorted(notes, key=lambda x: int(x.split("-")[0]))
removed_priority = [element.split("-")[1] for element in sorted_notes]

#split
#get only index 1
# append list

print(removed_priority)
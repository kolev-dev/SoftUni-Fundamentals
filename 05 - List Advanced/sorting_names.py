names_sequence = input().split(", ")

sorted_names = sorted(names_sequence, key= lambda x: (-len(x), x))

print(sorted_names)
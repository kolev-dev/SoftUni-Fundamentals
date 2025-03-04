elements = input().split()
items_search = input().split()

bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    quantity = int(elements[i + 1])

    bakery[key] = quantity


for item in items_search:

    if item in bakery.keys():
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
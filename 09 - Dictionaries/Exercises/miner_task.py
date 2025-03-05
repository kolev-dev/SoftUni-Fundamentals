resources = {}

while True:
    material = input()
    if material == "stop":
        break
    quantity = int(input())

    if material not in resources.keys():
        resources[material] = 0
    resources[material] += quantity

for material, quantity in resources.items():
    print(f"{material} -> {quantity}")
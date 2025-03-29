materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ""

while True:
    input_materials = input().split()

    for i in range(0, len(input_materials), 2):
        quantity = int(input_materials[i])
        current_material = input_materials[i + 1].lower()

        if current_material not in materials.keys():
            materials[current_material] = 0
        materials[current_material] += quantity

        if materials["shards"] >= 250:
            legendary_item = "Shadowmourne obtained!"
            materials["shards"] -= 250

        elif materials["fragments"] >= 250:
            legendary_item = "Valanyr obtained!"
            materials["fragments"] -= 250

        elif materials["motes"] >= 250:
            legendary_item = "Dragonwrath obtained!"
            materials["motes"] -= 250


        if legendary_item:
            break

    if legendary_item:
        break

print(legendary_item)
for material, quantity in materials.items():
    print(f"{material}: {quantity}")



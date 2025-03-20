import re

bought_items = {}

text = input()
while text != "Purchase":
    pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
    matches = re.findall(pattern, text)

    if matches:
        item = matches[0][0]
        price = matches[0][1]
        quantity = matches[0][2]
        if item not in bought_items:
            bought_items[item] = 0
        bought_items[item] += float(price) * float(quantity)

    text = input()

print("Bought furniture:")
for item in bought_items.keys():
    print(item)

print(f"Total money spend: {sum(bought_items.values()):.2f}")

#.groups()
#re.search()

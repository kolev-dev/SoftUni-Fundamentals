products = {}
count_all_products = 0

while True:
    line = input().split(": ")


    if line[0] == "statistics":
        break

    product = line[0]
    quantity = int(line[1])

    count_all_products += quantity

    if product in products:
        products[product] += quantity

    else:
        products[product] = quantity


print("Products in stock:")
for p, q in products.items():
    print(f"- {p}: {q}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {count_all_products}")
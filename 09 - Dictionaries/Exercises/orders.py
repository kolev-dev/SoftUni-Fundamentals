bought_items = {}

while True:
        order = input()

        if order == "buy":
            break

        product, price, quantity = order.split()

        price = float(price)
        quantity = int(quantity)
    
        if product not in bought_items:
            bought_items[product] = []
            bought_items[product].append(price)
            bought_items[product].append(quantity)
        else:
            bought_items[product][0] = price
            bought_items[product][1] += quantity


for product, price_info in bought_items.items():
    #calculating price
    total_price = price_info[0] * price_info[1]
    print(f"{product} -> {total_price:.2f}")


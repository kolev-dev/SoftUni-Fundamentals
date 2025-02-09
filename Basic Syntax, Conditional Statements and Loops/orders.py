n = int(input())

total_price = 0


for order in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    # if 0 < price_per_capsule <= 100:
    #     pass
    # else:
    #     continue
    #
    # if 1 < days < 31:
    #     pass
    # else:
    #     continue
    #
    # if 1 < capsules_needed <= 2000:
    #     pass
    # else:
    #     continue

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_needed < 1 or capsules_needed > 2000:
        continue

    price = price_per_capsule * days * capsules_needed
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")


print(f"Total: ${total_price:.2f}")

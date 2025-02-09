coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00

def calculate_price(item, quantity):
    if item == "coffee":
        return coffee * quantity
    elif item == "water":
        return water * quantity
    elif item == "coke":
        return coke * quantity
    elif item == "snacks":
        return snacks * quantity

type_of_item = input()
quantity = int(input())
print(f"{calculate_price(type_of_item, quantity):.2f}")
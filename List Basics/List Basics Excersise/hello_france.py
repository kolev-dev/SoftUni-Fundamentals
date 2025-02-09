items_list = input().split("|")
budget = float(input())

profit = 0

price_for_clothes = 50.00
price_for_shoes = 35.00
price_for_accessories = 20.50

money_used_for_clothes = 0
money_used_for_shoes = 0
money_used_for_accessories = 0

for item in items_list:
    split_item = item.split("->")


    if split_item[0] == "Clothes":
        if float(split_item[1]) > price_for_clothes:
            pass
        else:
            if budget >= price_for_clothes:
                budget -= float(split_item[1])
                money_used_for_clothes += float(split_item[1])
            else:
                pass

    elif split_item[0] == "Shoes":
        if float(split_item[1]) > price_for_shoes:
            pass
        else:
            if budget >= price_for_shoes:
                budget -= float(split_item[1])
                money_used_for_shoes += float(split_item[1])
            else:
                pass


    elif split_item[0] == "Accessories":
        if float(split_item[1]) > price_for_accessories:
            pass
        else:
            if budget >= price_for_accessories:
                budget -= float(split_item[1])
                money_used_for_accessories += float(split_item[1])
            else:
                pass



# if budget >= profit:
#
#     print(f"Profit: {profit:.2f}")
#     print(f"Hello, France!")
# else:
#     print(f"Not enough money, you need ${profit - budget:.2f} more.")

list_before_increase = [money_used_for_clothes, money_used_for_shoes, money_used_for_accessories]

list_after_increase = []



for split_item in list_before_increase:
    increase = split_item * 1.4
    list_after_increase.append(increase)

print(*list_after_increase)
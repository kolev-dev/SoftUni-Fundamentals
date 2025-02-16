number_of_cities = int(input())

total_money = 0
total_expenses = 0


for city in range(1, number_of_cities + 1):
    current_city_name = input()
    money_earned = float(input())
    expenses = float(input())


    if city % 5 == 0:
        money_earned *= 0.9

    elif city % 3 == 0 :
        expenses *= 1.5

    total_money += money_earned
    total_expenses += expenses

    print(f"In {current_city_name} Burger Bus earned {money_earned - expenses:.2f} leva.")

print(f"Burger Bus total profit: {total_money - total_expenses:.2f} leva.")
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())


broken_helmet_count = lost_fights_count // 2
broken_sword_count = lost_fights_count // 3
broken_shield_count = lost_fights_count // (2 * 3)

broken_armor_count = broken_shield_count // 2

expenses = broken_helmet_count * helmet_price \
           + broken_sword_count * sword_price \
           + broken_shield_count * shield_price \
           + broken_armor_count * armor_price


print(f"Gladiator expenses: {expenses:.2f} aureus")


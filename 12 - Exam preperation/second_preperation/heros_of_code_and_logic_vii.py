# start time 14:43
heroes = {}

n = int(input())

for _ in range(n):
    info = input().split()
    hero, hit_points, mana = info
    heroes[hero] = {"hit_points": int(hit_points), "mana": int(mana)}

while True:
    command = input().split(" - ")

    action = command[0]

    if action == "End":
        break

    if action == "CastSpell":
        hero, mana_needed, spell_name = command[1:]
        if heroes[hero]["mana"] >= int(mana_needed):
            heroes[hero]["mana"] -= int(mana_needed)
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mana']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        hero, damage, attacker = command[1:]

        heroes[hero]["hit_points"] -= int(damage)

        if heroes[hero]["hit_points"] > 0: #alive
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hit_points']} HP left!")

        else:
            print(f"{hero} has been killed by {attacker}!")

    elif action == "Recharge":
        hero, amount = command[1:]
        mana_before_recharge = heroes[hero]["mana"]
        heroes[hero]["mana"] += int(amount)


        if heroes[hero]["mana"] >= 200:
            amount_recovered = min(int(amount), 200 - mana_before_recharge)
            heroes[hero]["mana"] = 200
        else:
            amount_recovered = amount



        print(f"{hero} recharged for {amount_recovered} MP!")

    elif action == "Heal":
        hero, amount = command[1:]
        hit_points_before_heal = heroes[hero]["hit_points"]
        heroes[hero]["hit_points"] += int(amount)


        if heroes[hero]["hit_points"] >= 100:
            amount_recovered = min(int(amount), 100 - hit_points_before_heal)
            heroes[hero]["hit_points"] = 100
        else:
            amount_recovered = amount



        print(f"{hero} healed for {amount_recovered} HP!")


for hero in heroes.keys():
    if heroes[hero]["hit_points"] > 0:
        print(hero)
        print(f"  HP: {heroes[hero]['hit_points']}")
        print(f"  MP: {heroes[hero]['mana']}")


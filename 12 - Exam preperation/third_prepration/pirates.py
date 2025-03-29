locations = {}

while True:
    command = input().split("||")

    if command[0] == 'Sail':
        break

    city, population, gold = command

    if city not in locations:
        locations[city] = {"population": 0, "gold": 0}

    locations[city]["population"] += int(population)
    locations[city]["gold"] += int(gold)

while True:
    event_info = input().split("=>")

    event = event_info[0]

    if event == "End":
        break

    if event == "Plunder":
        town, people, gold = event_info[1:]

        locations[town]["population"] -= int(people)
        locations[town]["gold"] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if locations[town]["population"] == 0 or locations[town]["gold"] == 0:
            del locations[town]
            print(f"{town} has been wiped off the map!")

    elif event == "Prosper":
        town, gold = event_info[1:]

        if int(gold) < 0:
            print("Gold added cannot be a negative number!")

        else:
            locations[town]["gold"] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {locations[town]['gold']} gold.")



if locations:
    print(f"Ahoy, Captain! There are {len(locations)} wealthy settlements to go to: ")
    for town, nested_dict in locations.items():
        print(f"{town} -> Population: {nested_dict['population']} citizens, Gold: {nested_dict['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
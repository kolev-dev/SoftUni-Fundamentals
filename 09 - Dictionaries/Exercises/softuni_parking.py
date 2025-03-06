parking_lot = {}

n = int(input())

for _ in range(n):
    operation = input().split()

    action = operation[0] # register or unregister

    if action == "register":
        name, plate_number = operation[1], operation[2]

        if name in parking_lot.keys():
            print(f"ERROR: already registered with plate number {parking_lot[name]}")
        else:
            parking_lot[name] = plate_number
            print(f"{name} registered {plate_number} successfully")

    elif action == "unregister":
        name = operation[1]

        if name not in parking_lot.keys():
            print(f"ERROR: user {name} not found")
        else:
            del parking_lot[name]
            print(f"{name} unregistered successfully")

for username, plate in parking_lot.items():
    print(f"{username} => {plate}")


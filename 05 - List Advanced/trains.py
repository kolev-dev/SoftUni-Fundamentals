wagons = int(input())

train = [0] * wagons
while True:
    command = input().split()

    if command[0] == "End":
        break

    elif command[0] == "add":
        last_wagon = wagons - 1
        people = int(command[1])
        train[last_wagon] += people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

print(train)
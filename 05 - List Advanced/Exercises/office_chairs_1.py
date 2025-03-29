number_of_rooms = int(input())


total_chairs_unoccupied = 0
needed_chairs_at_least_once = False

for room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()

    if len(chairs) < int(visitors):
        print(f"{abs(len(chairs) - int(visitors))} more chairs needed in room {room}")
        needed_chairs_at_least_once = True
    else:
        total_chairs_unoccupied += len(chairs) - int(visitors)


if not needed_chairs_at_least_once:
    print(f"Game On, {total_chairs_unoccupied} free chairs left")
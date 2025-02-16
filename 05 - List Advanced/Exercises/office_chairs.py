number_of_rooms = int(input())
total_chairs = 0
total_people = 0

for room in range(1, number_of_rooms + 1):
    chairs, people = input().split()
    total_chairs += len(chairs)
    total_people += int(people)

    difference = len(chairs) - int(people)

    #not enough chairs
    if len(chairs) < int(people):
        print(f"{abs(difference)} more chairs needed in room {room}")



if total_chairs > total_people:
    print(f"Game On, {abs(total_chairs - total_people)} free chairs left")

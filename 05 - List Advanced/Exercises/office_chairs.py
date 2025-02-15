number_of_rooms = int(input())
total_chairs = 0

for room in range(1, number_of_rooms + 1):
    chairs, people = input().split()



    difference = len(chairs) - int(people)

    #not enough chairs
    if len(chairs) < int(people):
        print(f"{abs(difference)} more chairs needed in room {room}")

    elif chairs > people:
        print(f"Game On, {abs(total_chairs)} free chairs left")

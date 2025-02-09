n = int(input())

#not a constant
tank_capacity = 255

for _ in range(n):
    litters = int(input())

    if tank_capacity - litters < 0:
        print("Insufficient capacity!")
        continue

    tank_capacity -= litters

print(255 - tank_capacity)







#wrong code here

# n = int(input())
#
# #not a constant
# tank_capacity = 255
#
# for _ in range(n):
#     litters = int(input())
#
#     if tank_capacity - litters > 0:
#         tank_capacity -= litters
#     else:
#         print("Insufficient capacity!")
#         continue
#
#
# print(255 - tank_capacity)


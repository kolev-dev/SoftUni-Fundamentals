age = int(input())

# if age > 21:
#     print("drink whisky")
# elif age < 13:
#     print("drink toddy")
# elif age < 18:
#     print("drink coke")
# elif age <= 21:
#     print("drink beer")

if age <= 14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age < 21:
    print("drink beer")
elif age > 21:
    print("drink whisky")
# def checks(racer_list):
#     zero_flag = False
#     racer_sum = 0
#     if num == 0:
#         zero_flag = True
#     if num != 0:
#         racer_sum += num
#     if zero_flag:
#         racer_sum *= 0.8
#         zero_flag = False
#
#     return racer_sum

minutes_race = list(map(int, input().split()))

per_racer = len(minutes_race) // 2

left_racer = [minutes_race[i] for i in range(0, per_racer)]
right_racer = [minutes_race[i] for i in range(per_racer + 1, len(minutes_race))]

left_racer_result = 0
right_racer_result = 0


for num in left_racer:
    if num == 0:
        left_racer_result *= 0.8
    if num != 0:
        left_racer_result += num

for num in right_racer[::-1]:
    if num == 0:
        right_racer_result *= 0.8
    if num != 0:
        right_racer_result += num

if right_racer_result > left_racer_result:
    print(f"The winner is left with total time: {left_racer_result:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_result:.1f}")
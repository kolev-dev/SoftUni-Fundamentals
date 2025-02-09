n = int(input())

max_value = 0
max_weight = 0
max_time_needed = 0
max_quality = 0


for ball in range(n):
    ball_weight = int(input())
    ball_time_needed = int(input())
    ball_quality = int(input())

    current_ball_value = (ball_weight / ball_time_needed) ** ball_quality

    if current_ball_value > max_value:
        max_value = current_ball_value
        max_weight = ball_weight
        max_time_needed = ball_time_needed
        max_quality = ball_quality


print(f" {max_weight} : {max_time_needed} = {int(max_value)} ({max_quality})")

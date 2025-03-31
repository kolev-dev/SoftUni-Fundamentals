def check_and_add_to_records(user: str):
    if user not in followers:
        followers[username] = {"likes": 0, "comments": 0}

followers = {}

while True:
    command = input().split(": ")

    action = command[0]

    if action == "Log out":
        break

    if action == "New follower":
        username = command[1]
        check_and_add_to_records(username)

    elif action == "Like":
        username, count = command[1:]

        check_and_add_to_records(username)
        followers[username]["likes"] += int(count)

    elif action == "Comment":
        username = command[1]

        check_and_add_to_records(username)
        followers[username]["comments"] += 1

    elif action == "Blocked":
        username = command[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")


print(f"{len(followers)} followers")
for username, count in followers.items():
    total_count = count["likes"] + count["comments"]
    print(f"{username}: {total_count}")
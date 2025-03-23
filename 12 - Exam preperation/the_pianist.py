n = int(input())

collection = {}

for i in range(n):
    piece, composer, key = input().split("|")
    collection[piece] = {"composer": composer, "key": key}

while True:
    command = input().split("|")

    if command[0] == "Stop":
        break

    # action, piece, composer, key = input().split("|")
    action = command[0]
    if action == "Add":
        piece, composer, key = command[1:]
        if piece in collection:
            print(f"{piece} is already in the collection!")
            continue
        collection[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = command[1]
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece, new_key = command[1:]
        if piece in collection:
            collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key in collection.keys():
    print(f"{key} -> Composer: {collection[key]['composer']}, Key: {collection[key]['key']}")
from time import process_time_ns

while True:
    word = input()


    if word == "End":
        break

    if word == "SoftUni":
        pass
    else:
        for ch in word:
            print(ch * 2, end = "")

        print("")


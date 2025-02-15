#first solution
#
# version = list(map(int, input().split(".")))
#
# number_as_str = f"{version[0]}{version[1]}{version[2]}"
# number_as_int = int(number_as_str) + 1
#
# print(".".join([string for string in str(number_as_int)]))
#



#second solution
version = list(map(int, input().split(".")))
version[-1] +=1

for index in range(len(version) - 1,-1,-1):
    if version[index] == 10:
        version[index] = 0
        version[index - 1] +=1

print(".".join(list(map(str, version))))

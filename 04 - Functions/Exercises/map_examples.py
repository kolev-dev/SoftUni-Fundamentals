def get_len(word):
    return len(word)


lst =  input().split()

x = map(get_len, lst)

print(list(x))



tail = input()
body = input()
head = input()

lst = [tail, body, head]

lst[0], lst[2] = lst[2], lst[0]

print(lst)
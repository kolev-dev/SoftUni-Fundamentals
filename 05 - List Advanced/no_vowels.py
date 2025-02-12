word = input()

lst = [letter for letter in word if letter.lower() not in 'a''o''u''e''i']
print("".join(lst))


def get_len(word):
    return len(word)


lst =  input().split()

x = map(get_len, lst)
#1.     - The `map()` function applies a given function to each item
# in an **iterable** (like a list, tuple, etc.) and returns an iterator.

print(list(x))



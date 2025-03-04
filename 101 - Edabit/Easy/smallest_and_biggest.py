def min_max(lst: list) -> list:
    min_value = min(lst)
    max_value = max(lst)
    return [min_value, max_value]


list_input = eval(input())
print(min_max(list_input))

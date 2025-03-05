first_list = ["a", "b", "c"]
second_list = [1, 2, 3]

my_dict = {key:value for key, value in zip(first_list, second_list)}
print(my_dict)
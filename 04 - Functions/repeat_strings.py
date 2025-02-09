# def repeat_strings(string, times):
#     return string * times
#
# string_input = input()
# n = int(input())
# print(repeat_strings(string_input, n))




# using lambda
string_input = input()
n = int(input())

repeat_string = lambda string_input, n: string_input * n
print(repeat_string(string_input, n))
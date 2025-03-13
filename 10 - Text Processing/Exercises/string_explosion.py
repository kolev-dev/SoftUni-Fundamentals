text = input()
final_string = ""
strength = 0

for index in range(len(text)):
   if strength > 0 and text[index] != ">":
       strength -= 1

   elif text[index] == ">":
       final_string += ">"
       strength += int(text[index + 1])
   else:
       final_string += text[index]

print(final_string)
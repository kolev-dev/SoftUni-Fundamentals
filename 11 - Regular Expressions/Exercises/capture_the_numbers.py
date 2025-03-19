import re

text = input()
pattern = r"\d+"

while text:
    matches = re.findall(pattern, text)
    if matches:
        print(" ".join(matches), end = " ")

    text = input()




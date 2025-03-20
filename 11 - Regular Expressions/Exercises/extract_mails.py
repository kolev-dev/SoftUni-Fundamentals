import re

text = input()
pattern = r"(\s[a-z][a-z\-\.]+@[a-z]([a-z\-]*)+(\.[a-z]+)+)"

matches = re.findall(pattern, text)
for match in matches:
    print(match[0])


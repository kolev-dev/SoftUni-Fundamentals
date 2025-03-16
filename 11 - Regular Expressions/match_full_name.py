import re

name = input()
set_of_names = set(re.findall(r"\b[A-Z]{1}[a-z]*\b", name))
print(" ".join(set_of_names))
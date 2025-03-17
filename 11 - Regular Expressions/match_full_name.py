import re

names = input()
set_of_names = re.findall(r"\b[A-Z][a-z]* [A-Z][a-z]*\b", names)
print(" ".join(set_of_names))

# \b[A-Z]{1}[a-z] [A-Z]{1}[a-z]*\b
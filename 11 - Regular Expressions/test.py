import re

text = "Hello _id, I'm _good"

matches = re.findall(r"\b_([A-Za-z0-9]+)\b", text)
print(",".join(matches))
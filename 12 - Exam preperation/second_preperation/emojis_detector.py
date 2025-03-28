# import re
# from functools import reduce
#
# text = input()
#
# # Calculate cool threshold
# digits = [int(d) for d in re.findall(r'\d', text)]
# cool_threshold = reduce(lambda x, y: x * y, digits, 1)
# print(f"Cool threshold: {cool_threshold}")
#
# # Find emojis
# pattern = re.compile(r'(\*\*|::)([A-Z][a-z]{2,})\1')
# emojis = pattern.findall(text)
# print(f"{len(emojis)} emojis found in the text. The cool ones are:")
#
# # Filter and print cool emojis
# cool_emojis = [f"{match[0]}{match[1]}{match[0]}" for match in emojis if sum(ord(char) for char in match[1]) > cool_threshold]
# if cool_emojis:
#     print("\n".join(cool_emojis))



# NOT VALID
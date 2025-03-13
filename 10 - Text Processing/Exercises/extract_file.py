file_path = input().split("\\")

file_info = file_path[-1].split(".")

print(f"File name: {file_info[0]}")
print(f"File extension: {file_info[1]}")
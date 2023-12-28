path_file = input().split("\\")
name, extension = path_file[-1].split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")
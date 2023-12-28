# version_str = input()
# version_int = int(version_str.replace(".", ""))
# next_version_int = version_int + 1
# next_version_str = ".".join(str(next_version_int))
# print(next_version_str)

version = [int(x) for x in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9 and version[index - 1] != 0:
        version[index] = 0
        version[index - 1] += 1
# print('.'.join((str(x) for x in version)))
print(*version, sep=".")

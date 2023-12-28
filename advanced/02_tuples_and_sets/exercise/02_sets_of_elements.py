numbers = [int(x) for x in input().split()]
sets_of_elements = []

for num in range(len(numbers)):
    sets_of_elements.append(set())
    for sets in range(numbers[num]):
        number = int(input())
        sets_of_elements[num].add(number)
repeat_elements = sets_of_elements[0].intersection(sets_of_elements[1])
print(*repeat_elements, sep="\n")
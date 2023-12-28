def negative_vs_positive(list_with_numbers):
    dict_nums = {'positives': 0, 'negatives': 0}
    for num in list_with_numbers:
        if num > 0:
            dict_nums['positives'] += num
        else:
            dict_nums['negatives'] += num
    print(dict_nums['negatives'])
    print(dict_nums['positives'])
    dict_nums['negatives'] = abs(dict_nums['negatives'])

    return f"The {max(dict_nums, key=dict_nums.get)} are stronger than the {min(dict_nums, key=dict_nums.get)}"


numbers = [int(num) for num in input().split()]
print(negative_vs_positive(numbers))
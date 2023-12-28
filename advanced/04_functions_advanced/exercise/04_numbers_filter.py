def even_odd_filter(**kwargs):
    for key, values in kwargs.items():
        if key == 'odd':
            kwargs['odd'] = [int(x) for x in values if x % 2 != 0]
        else:
            kwargs['even'] = [int(x) for x in values if x % 2 == 0]
    return dict(sorted(kwargs.items()))


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))


def age_assignment(*args, **kwargs):
    result = ""
    for name in sorted(args):
        if name[0:1] in kwargs:
            age = kwargs[name[0:1]]
            result += f"{name} is {age} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
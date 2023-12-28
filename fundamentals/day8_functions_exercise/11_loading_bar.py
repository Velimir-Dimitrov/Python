def loading_bar(some_number):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loading_percentage = some_number // 10
    return f"{some_number}% [{'%' * loading_percentage}{'.' * (10 - loading_percentage)}]\nStill loading..."


number = int(input())
print(loading_bar(number))


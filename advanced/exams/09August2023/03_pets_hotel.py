def accommodate_new_pets(capacity, weight, *args):
    accommodate_pets_dict = {}
    accommodate_capacity = capacity
    accommodate_weight = weight
    ignored = 0
    pets = args
    result = ''
    for pet, pet_weight in pets:
        if accommodate_capacity == 0:
            result += "You did not manage to accommodate all pets!\n"
            break
        elif accommodate_weight < float(pet_weight):
            ignored += 1
            continue

        if pet not in accommodate_pets_dict:
            accommodate_pets_dict[pet] = 0
        accommodate_pets_dict[pet] += 1
        accommodate_capacity -= 1

    if capacity - accommodate_capacity == len(pets) - ignored:
        result += f"All pets are accommodated! Available capacity: {accommodate_capacity}.\n"

    result += "Accommodated pets:\n"
    for key, value in sorted(accommodate_pets_dict.items()):
        result += f'{key}: {value}\n'
    return result


print(accommodate_new_pets(10, 15.0, ("cat", 5.8), ("dog", 10.0), ))
print(accommodate_new_pets(10, 10.0, ("cat", 5.8), ("dog", 10.5), ("parrot", 0.8), ("cat", 3.1), ))
print(accommodate_new_pets(2, 15.0, ("dog", 10.0), ("cat", 5.8), ("cat", 2.7), ))
print(accommodate_new_pets(10, 15.0, ("cat", 16.8), ("dog", 16.0), ))

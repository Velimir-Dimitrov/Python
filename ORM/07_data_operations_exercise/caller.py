import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character
# Create queries within functions


def create_pet(name: str, species: str) -> str:
    Pet.objects.create(
        name=name,
        species=species
    )
    return f"{name} is a very cute {species}!"

# Test code
# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()

# Test code
# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)
# delete_all_artifacts()


def show_all_locations() -> str:
    return "\n".join(str(location) for location in Location.objects.all().order_by("-id"))


def new_capital() -> None:
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location() -> None:
    Location.objects.first().delete()


# Test code
# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount() -> None:
    cars = Car.objects.all()
    for car in cars:
        percentage_off = sum(int(d) for d in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
    Car.objects.bulk_update(cars, ['price_with_discount'])


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


# Test code
# apply_discount()
# print(get_recent_cars())


def show_unfinished_tasks() -> str:
    return "\n".join(str(t) for t in Task.objects.filter(is_finished=False))


def complete_odd_tasks() -> None:
    tasks = Task.objects.filter(is_finished=False)
    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str) -> None:
    encoded_text = ''.join(chr(ord(char) - 3) for char in text)
    Task.objects.filter(title=task_title).update(description=encoded_text)


# Test code
# Task.objects.create(
#     title="Simple Task",
#     description="This is a sample task description",
#     due_date="2023-10-31",
#     is_finished=False
# )
# encode_and_replace("Zdvk#wkh#glvkhv$","Simple Task")
# print(Task.objects.get(title='Simple Task').description)


def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    return "\n".join(str(room) for room in deluxe_rooms if room.id % 2 == 0)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")
    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue
        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id
        previous_room_capacity = room.capacity
    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved=True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if not last_room.is_reserved:
        last_room.delete()


# Test code
# HotelRoom.objects.create(room_number=401, room_type="Standart", capacity=2, amenities="Tv", price_per_night=100.00)
# HotelRoom.objects.create(room_number=501, room_type="Deluxe", capacity=3, amenities="Wi-Fi", price_per_night=200.00)
# HotelRoom.objects.create(room_number=601, room_type="Deluxe", capacity=6, amenities="Jacuzzi", price_per_night=400.00)
# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=401).is_reserved)


def update_characters() -> None:
    Character.objects.filter(class_name="Mage").update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name="Warrior").update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty"
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    Character.objects.create(
        name=first_character.name + " " + second_character.name,
        class_name = "Fusion",
        level = (first_character.level + second_character.level) // 2,
        strength = (first_character.strength + second_character.strength) * 1.2,
        dexterity = (first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence = (first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points = first_character.hit_points + second_character.hit_points,
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
            if first_character.class_name in ["Mage", "Scout"]
            else "Dragon Scale Armor, Excalibur"
    )
    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()


# Test code
# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
# )
#
# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection',
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)


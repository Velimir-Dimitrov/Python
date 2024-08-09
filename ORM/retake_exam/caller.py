import os


import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import House, Dragon, Quest
from django.db.models import Q, Count, F, Min


# Create queries within functions


def get_houses(search_string=None) -> str:
    if search_string is None:
        return "No houses match your search."

    query = Q(name__icontains=search_string) | Q(motto__icontains=search_string)
    houses = House.objects.filter(query).order_by('-wins', 'name')

    if not houses:
        return "No houses match your search."

    result = []

    for h in houses:
        if h.motto:
            house_motto = h.motto
        else:
            house_motto = "N/A"
        result.append(f"House: {h.name}, wins: {h.wins}, motto: {house_motto}")

    return "\n".join(result)


def get_most_dangerous_house() -> str:
    most_dangerous_house = House.objects.get_houses_by_dragons_count().first()

    if not most_dangerous_house or most_dangerous_house.num_dragons == 0:
        return ""

    return f"The most dangerous house is the House of {most_dangerous_house.name} with {most_dangerous_house.num_dragons} dragons. Currently {'ruling' if most_dangerous_house.is_ruling else 'not ruling'} the kingdom."


def get_most_powerful_dragon() -> str:
    found_dragon = Dragon.objects.filter(is_healthy=True).order_by('-power', 'name').first()

    if not found_dragon:
        return "No relevant data."

    num_quests = found_dragon.quests.count()
    house_name = found_dragon.house.name

    return f"The most powerful healthy dragon is {found_dragon.name} with a power level of {found_dragon.power}, breath type {found_dragon.breath}, and {found_dragon.wins} wins, coming from the house of {house_name}. Currently participating in {num_quests} quests."


def update_dragons_data():
    updated_dragons = Dragon.objects.filter(
        is_healthy=False,
        power__gt=1.0
    ).update(
        power=F('power') - 0.1,
        is_healthy=True,
    )

    if updated_dragons == 0:
        return "No changes in dragons data."

    all_dragons = Dragon.objects.annotate(
        min_power=Min('power'))

    return f"The data for {updated_dragons} dragon/s has been changed. The minimum power level among all dragons is {all_dragons.min_power:.1f}"


def get_earliest_quest():
    earliest_quest = Quest.objects.prefetch_related("dragons").order_by('-start_time').first()

    if earliest_quest is None:
        return "No relevant data."

    host_name = earliest_quest.host.name
    dragons = "*".join(f'{d.name}' for d in earliest_quest.dragons.all().order_by("-power", "name"))
    num_dragons = earliest_quest.dragons.count()
    avg_power_level = sum([d.power for d in earliest_quest.quest_set.all()]) / num_dragons if num_dragons else 0.00
    start_date = earliest_quest.start_time.date().strftime("%d.%m.%Y")

    return f"The earliest quest is: {earliest_quest.name}, code: {earliest_quest.code}, start date: {start_date}, host: {host_name}. Dragons: {dragons}. Average dragons power level: {avg_power_level:.2f}"

import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission
from django.db.models import Q, Count, F, Avg


# Create queries within functions


def get_astronauts(search_string=None) -> str:
    if search_string is None:
        return ""

    query = Q(phone_number__icontains=search_string) | Q(name__icontains=search_string)
    found_astronauts = Astronaut.objects.filter(query).order_by("name")

    if not found_astronauts:
        return ""

    result = []
    for a in found_astronauts:
        status = ""
        if a.is_active:
            status = "Active"
        else:
            status = "Inactive"
        result.append(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {status}")

    return "\n".join(result)


def get_top_astronaut() -> str:
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not top_astronaut or top_astronaut.num_missions == 0:
        return "No Data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.num_missions} missions"


def get_top_commander() -> str:
    top_commander = Astronaut.objects.annotate(
        count_commander=Count(
            "commanders"
        )
    ).order_by("-count_commander", "phone_number")[:1][0]

    if not top_commander or not top_commander.count_commander:
        return "No Data."

    return f"Top Commander: {top_commander.name} with {top_commander.count_commander} commanded missions."


def get_last_completed_mission() -> str:
    last_completed_mission = Mission.objects.filter(status="Completed").last()

    if not last_completed_mission:
        return "No data."

    astronauts = last_completed_mission.astronauts.order_by("name")
    last_completed_mission_astronauts = []
    total_spacewalks = 0

    for a in astronauts:
        last_completed_mission_astronauts.append(a.name)
        total_spacewalks += a.spacewalks

    return (f"The last completed mission is: {last_completed_mission.name}."
            f" Commander: {last_completed_mission.commander.name if True else "TBA"}. "
            f"Astronauts: {', '.join(last_completed_mission_astronauts)}."
            f" Spacecraft: {last_completed_mission.spacecraft.name}."
            f" Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft() -> str:
    most_used_spacecraft = Spacecraft.objects.annotate(num_missions=Count("spacecrafts")).order_by("-num_missions", "name").first()

    if not most_used_spacecraft or most_used_spacecraft.num_missions == 0:
        return "No data."

    num_astronauts = len(most_used_spacecraft.astronauts.distict())

    return (f"The most used spacecraft is: {most_used_spacecraft.name},"
            f" manufactured by {most_used_spacecraft.manufacturer}, used in {most_used_spacecraft.num_missions} missions,"
            f" astronauts on missions: {num_astronauts}.")


def decrease_spacecrafts_weight()-> str:
    update_spacecrafts = Spacecraft.objects.prefetch_related(
        "spacecrafts").filter(
        spacecrafts__status="Planned", weight__gte=200.0
    ).distinct().update(weight= F('weight') - 200.0)

    avg_weight = Spacecraft.objects.aggregate(Avg('weight'))

    if not update_spacecrafts:
        return "No changes in weight."

    return f"The weight of {update_spacecrafts} spacecrafts has been decreased. The new average weight of all spacecrafts is {avg_weight:.1f}kg"


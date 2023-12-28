days_period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for days in range(1, days_period + 1):
    patients_per_day = int(input())
    if days % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients_per_day <= doctors:
        treated_patients += patients_per_day
    elif patients_per_day > doctors:
        treated_patients += doctors
        untreated_for_the_day = patients_per_day - doctors
        untreated_patients += untreated_for_the_day
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
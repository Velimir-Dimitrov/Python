exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_total = exam_hour * 60 + exam_minutes
arrival_total = arrival_hour * 60 + arrival_minutes
diff = abs(arrival_total - exam_total)
hh = diff // 60
mm = diff % 60

if exam_total < arrival_total:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    elif diff >= 60:
        print(f"{hh}:{mm:02d} hours after the start")
elif diff <= 30:
    if diff == 0:
        print("On time")
    elif diff < 60:
        print("On time")
        print(f"{diff} minutes before the start")
elif exam_total > arrival_total and diff > 30:
    print("Early")
    if 30 < diff < 60:
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        print(f"{hh}:{mm:02d} hours before the start")

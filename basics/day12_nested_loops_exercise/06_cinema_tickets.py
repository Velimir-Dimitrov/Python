movie = input()

total_tickets = 0
standard_seats = 0
student_seats = 0
kid_seats = 0

while movie != "Finish":
    seats = int(input())
    movie_tickets = 0
    while seats > movie_tickets:
        tickets = input()
        if tickets == "End":
            break
        movie_tickets += 1
        total_tickets += 1
        if tickets == "standard":
            standard_seats += 1
        elif tickets == "student":
            student_seats += 1
        elif tickets == "kid":
            kid_seats += 1
    print(f"{movie} - {movie_tickets / seats * 100:.2f}% full.")
    movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_seats / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_seats / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_seats / total_tickets * 100:.2f}% kids tickets.")

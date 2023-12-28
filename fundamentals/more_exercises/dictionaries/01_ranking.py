def validity_check(con_name, con_password, dictionary_with_contests):
    if con_name in dictionary_with_contests and dictionary_with_contests[con_name] == con_password:
        return True
    return False


def save_user(con_name, con_candidate, con_points, dictionary_with_candidates):
    if con_candidate in dictionary_with_candidates:
        if con_name in dictionary_with_candidates[con_candidate] and dictionary_with_candidates[con_candidate][con_name] >= con_points:
            return dictionary_with_candidates
        dictionary_with_candidates[con_candidate][con_name] = con_points
        return  dictionary_with_candidates
    dictionary_with_candidates[con_candidate] = {con_name:con_points}
    return dictionary_with_candidates


command = input()
contests_dict = {}
candidates_dict = {}

while command != "end of contests":
    contest, password = command.split(":")
    contests_dict[contest] = password
    command = input()

while True:
    submission = input()
    if submission == "end of submissions":
        break
    contest_name, contest_password, contest_candidate, contest_points = [int(x) if x.isdigit() else x for x in submission.split("=>")]
    if validity_check(contest_name, contest_password, contests_dict):
        candidates_dict = save_user(contest_name, contest_candidate, contest_points, candidates_dict)


sorted_candidates = dict(sorted(candidates_dict.items()))

best_candidate = ""
best_points = 0
for candidate in candidates_dict:
    total_points = 0
    for contest in candidates_dict[candidate]:
        current_points = candidates_dict[candidate][contest]
        total_points += int(current_points)
    if best_points < total_points:
        best_candidate = candidate
        best_points = total_points
print(f"Best candidate is {best_candidate} with total {best_points} points.")

print("Ranking:")
for candidate in sorted_candidates:
    print(candidate)
    contests = dict(sorted(sorted_candidates[candidate].items(), key=lambda x:x[1], reverse=True))
    for contest in contests:
        points = contests[contest]
        print(f"#  {contest} -> {points}")

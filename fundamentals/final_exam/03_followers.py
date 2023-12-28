def adding_follower(follower_name, dictionary_with_followers):
    if follower_name in dictionary_with_followers:
        return dictionary_with_followers
    dictionary_with_followers[follower_name] = {"Likes": 0, "Comments": 0}
    return dictionary_with_followers


def adding_like(follower_name, number_of_likes, dictionary_with_followers):
    if follower_name not in dictionary_with_followers:
        dictionary_with_followers = adding_follower(follower_name, dictionary_with_followers)
    dictionary_with_followers[follower_name]["Likes"] += number_of_likes
    return dictionary_with_followers


def adding_comment(follower_name, dictionary_with_followers):
    if follower_name not in dictionary_with_followers:
        dictionary_with_followers = adding_follower(follower_name, dictionary_with_followers)
    dictionary_with_followers[follower_name]["Comments"] += 1
    return dictionary_with_followers


def blocking(follower_name, dictionary_with_followers):
    if follower_name not in dictionary_with_followers:
        print(f"{follower_name} doesn't exist.")
        return dictionary_with_followers
    del dictionary_with_followers[follower_name]
    return dictionary_with_followers


command = input()
facebook_dict = {}

while command != "Log out":
    if "follower" in command:
        action, username = command.split(": ")
        facebook_dict = adding_follower(username, facebook_dict)
    elif "Like" in command:
        action, username, count = command.split(": ")
        count_likes = int(count)
        facebook_dict = adding_like(username, count_likes, facebook_dict)
    elif "Comment" in command:
        action, username = command.split(": ")
        facebook_dict = adding_comment(username, facebook_dict)
    elif "Blocked" in command:
        action, username = command.split(": ")
        facebook_dict = blocking(username, facebook_dict)
    command = input()

number_of_followers = len(facebook_dict)

print(f"{number_of_followers} followers")
for follower in facebook_dict:
    likes = facebook_dict[follower]["Likes"]
    comments = facebook_dict[follower]["Comments"]
    total_sum = likes + comments
    print(f"{follower}: {total_sum}")

tail = input()
body = input()
head = input()

string_list = [tail, body, head]
string_list[0], string_list[2] = string_list[2], string_list[0]
print(string_list)
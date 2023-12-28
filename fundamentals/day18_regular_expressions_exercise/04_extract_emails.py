import re
text = input()
email_criteria = r"\b(?<!\-)(?<!\.)[A-Za-z0-9]+[._-]*[A-Za-z0-9]*\b@\b[A-za-z]+[-]*[A-za-z]+.[A-Za-z.]*\b[A-za-z]+\b"
found_emails = re.findall(email_criteria, text)
print(*found_emails, sep="\n")

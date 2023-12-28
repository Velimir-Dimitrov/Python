class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_NAME_MIN_SIZE = 5
valid_domains = ['.com', '.bg', '.net', '.org']

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split('@')[0]) < EMAIL_NAME_MIN_SIZE:
        raise NameTooShortError("Name must be more than 4 characters")

    if '.' + email.split('.')[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")



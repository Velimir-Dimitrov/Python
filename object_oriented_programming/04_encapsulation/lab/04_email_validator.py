class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def validate(self, email):
        a = EmailValidator.__is_name_valid(self, email.split('@')[0])
        b = EmailValidator.__is_mail_valid(self, email.split('@')[1].split('.')[0])
        c = EmailValidator.__is_domain_valid(self, email.split('@')[1].split('.')[-1])
        return all([a, b, c])

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains


# Test code:
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, name):
        valid_length = (5 <= len(name) <= 15)
        if not valid_length:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, psswrd):
        valid_length = len(psswrd) >= 8
        valid_upercase = any([x for x in psswrd if x.isupper()])
        valid_digits = any([x for x in psswrd if x.isdigit()])
        if not all((valid_length, valid_upercase, valid_digits)):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = psswrd

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
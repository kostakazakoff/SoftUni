def password_validation(password: str):
    def valid_length():
        if len(password) < 6 or len(password) > 10:
            print('Password must be between 6 and 10 characters')
            return False
        return True

    def only_letters_and_digits():
        if not password.isalnum():
            print('Password must consist only of letters and digits')
            return False
        return True

    def at_least_2_digits():
        pass_digits = list(x for x in password if x.isdigit())
        if len(pass_digits) < 2:
            print('Password must have at least 2 digits')
            return False
        return True
    
    valid = (valid_length(), only_letters_and_digits(), at_least_2_digits())
    
    if all(valid):
        print('Password is valid')


input_password = input()
password_validation(input_password)

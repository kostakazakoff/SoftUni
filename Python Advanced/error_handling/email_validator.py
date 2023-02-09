from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidSimbolsNumber(Exception):
    pass


class InvalidNameSymbols(Exception):
    pass


class InvalidDomainName(Exception):
    pass


valid_domains = ('.com', '.bg', '.net', '.org')
name_pattern = r'^[\w\.\d]+'
domain_pattern = r'[^ ][a-z0-9\-]{2,63}\.{1}[a-z]+$'

email = input()

while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    email = email.split('@')

    if len(email) > 2:
        raise InvalidSimbolsNumber('Email should contain only one @')

    username, domain_name = email

    if len(findall(name_pattern, username)[0]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if len(findall(name_pattern, username)[0]) != len(email[0]):
        raise InvalidNameSymbols('Email name should contain only letters, numbers, underscores and dots.')

    if not findall(domain_pattern, domain_name):
        raise InvalidDomainName('Domain name must contain between 2 and 63 characters - letters, numbers or hyphen(-) and no spaces')

    if not findall(domain_pattern, domain_name)[0].endswith(valid_domains):
        raise InvalidDomainError(f'Domain must be one of the following: {valid_domains}')

    print('Email is valid')

    email = input()

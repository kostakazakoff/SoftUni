def next_version(version: str):
    # input the version using 'map' function - converting the chars to integers:
    version = list(map(int, version.split('.')))
    # creating an integer by the values in version (for example - [1, 2, 3] = 123) and increasing with 1
    # The result is the next version list:
    return '.'.join([x for x in str(version[0] * 100 + version[1] * 10 + version[2] + 1)])


ver = input()
print(next_version(ver))

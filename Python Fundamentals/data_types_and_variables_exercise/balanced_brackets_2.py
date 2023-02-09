n = int(input())

# defining "brackets" and creating an empty list for them:
balanced = ('(', ')')
brackets = []

for _ in range(n):
    # check if the entry is bracket, if not - go to the beginning of iteration:
    entry = input()
    if not any(x in balanced for x in entry):
        continue
    # o.k. it's a bracket - append to the brackets list:
    brackets.append(entry)

# counting the opened brackets (expecting the same quantity of the closing one):
opened = brackets.count('(')
balanced = []
# using the count of opened brackets, creating a list of balanced brackets as they should be
# like this ['(', ')', '(', ')'...] - opening and closing bracket:
for i in range(opened):
    balanced.append('(')
    balanced.append(')')

# check if all opened brackets have a closed one (the 'balanced' list):
if brackets == balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

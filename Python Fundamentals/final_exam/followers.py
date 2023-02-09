def new_follower():
    global followers, username, LIKES, COMMENTS
    if username in followers:
        return
    followers.update({username: {LIKES: 0, COMMENTS: 0}})


def like():
    global followers, username, LIKES, COMMENTS, count
    if username not in followers:
        followers.update({username: {LIKES: 0, COMMENTS: 0}})
    followers[username][LIKES] += count


def comment():
    global followers, username, LIKES, COMMENTS
    if username not in followers:
        followers.update({username: {LIKES: 0, COMMENTS: 0}})
    followers[username][COMMENTS] += 1


def block():
    global followers, username, LIKES, COMMENTS
    if username not in followers:
        print(f"{username} doesn't exist.")
        return
    del followers[username]


followers = {}
LIKES = 'Likes'
COMMENTS = 'Comments'
command = input()

while command != 'Log out':
    action, *info = command.split(': ')
    if action == 'New follower':
        username = info[0]
        new_follower()
    elif action == 'Like':
        username, count = info[0], int(info[1])
        like()
    elif action == 'Comment':
        username = info[0]
        comment()
    elif action == 'Blocked':
        username = info[0]
        block()
    command = input()

print(f'{len(followers)} followers')
if followers:
    [print(f'{name}: {v[LIKES] + v[COMMENTS]}') for name, v in followers.items()]

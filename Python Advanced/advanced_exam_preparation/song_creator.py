def add_songs(*args):
    output = ''
    playlist = {}
    for song in args:
        title, lyrics = song[0], song[1]
        if title not in playlist:
            playlist.update({title: []})
        [playlist[title].append(l) for l in lyrics if l not in playlist[title]]
    for title, lyrics in playlist.items():
        lyrics = '\n'.join([x for x in lyrics])
        output += f'- {title}\n'
        if lyrics:
            output += f'{lyrics}\n'
    return output


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
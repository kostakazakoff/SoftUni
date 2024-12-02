import re

html_string = input()

head = ''.join(re.findall(r'<title>(.*)<\/title>', html_string))
result = re.split(r'<title>.*<\/title>|<p>|<\/p>|<a>|<\/a>|\\n|<a href=".+">|<html>|<\/html>|<body>|<\/body>|<head>|<\/head>', html_string)
result = ''.join([x for x in result if x])

print(f'Title: {head}')
print(f"Content: {result}")
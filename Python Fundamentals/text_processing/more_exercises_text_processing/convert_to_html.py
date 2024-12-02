def convert_to_html(head: str, article: str, divs: list):
    divs = ''.join([f'<div>\n    {text}\n</div>\n' for text in divs])
    print(f'<h1>\n    {head}\n</h1>\n<article>\n    {article}\n</article>\n{divs}')


head_to_enter = input()
article_to_enter = input()
comments = []
comment = input()
while comment != 'end of comments':
    comments.append(comment)
    comment = input()

convert_to_html(head_to_enter, article_to_enter, comments)

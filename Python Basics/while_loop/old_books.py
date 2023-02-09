the_book = input()
book = input()
there_is_no_more_books = False
search_counter = 0
while book != the_book:
    if book == 'No More Books':
        there_is_no_more_books = True
        break
    search_counter += 1
    book = input()

if there_is_no_more_books:
    print('The book you search is not here!')
    print(f'You checked {search_counter} books.')
else:
    print(f'You checked {search_counter} books and found it.')
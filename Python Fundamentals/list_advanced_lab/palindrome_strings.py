def palindromes(string: str, palindrome_to_search: str):
    string = string.split()
    palindrome_words =  [word for word in string if word == word[::-1]]
    palindrome_count = palindrome_words.count(palindrome_to_search)
    return palindrome_words, palindrome_count


entry_string = input()
searched_palindrome = input()
p_words, p_count = palindromes(entry_string, searched_palindrome)
print(p_words)
print(f"Found palindrome {p_count} times")
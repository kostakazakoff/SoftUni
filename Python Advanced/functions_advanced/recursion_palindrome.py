def palindrome(text: str, index: int):
    half = len(text) // 2
    if index == half:
        return f'{text} is a palindrome'
    if text[index] != text[-1 - index]:
        return f'{text} is not a palindrome'
    return palindrome(text, index + 1)


print(palindrome("abcddcba", 0))
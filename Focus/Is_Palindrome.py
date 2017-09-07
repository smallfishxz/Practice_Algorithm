def is_palindrome(s):
    """Returns True if the input string is a palindrome, else False."""

    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalpha():
            i += 1
            continue
        elif not s[j].isalpha():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

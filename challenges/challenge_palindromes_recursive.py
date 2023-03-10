def is_palindrome_recursive(word, low_index=0, high_index=0):
    if not word:
        return False

    if len(word) < 1:
        return word
    else:
        return is_palindrome_recursive(word[1:]) + [word[0]]

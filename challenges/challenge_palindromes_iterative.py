def is_palindrome_iterative(word):
    reverse_word = [word]

    for letter in word:
        reverse_word.insert(0, letter)

    return reverse_word

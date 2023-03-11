def reversing_word(word):
    new_word = []
    for letter in word:
        new_word.insert(0, letter)

    return new_word


def is_palindrome_iterative(word):
    if not word or len(word) == 0 or type(word) != str:
        return False

    if len(word) == 1:
        return True

    original_word = word
    final_word = "".join(reversing_word(list(word)))

    if original_word == final_word:
        return True
    else:
        return False

def reversing_word(word):
    if len(word) == 1:
        return word
    else:
        return reversing_word(word[1:]) + [word[0]]


def is_palindrome_recursive(word, low_index=0, high_index=0):
    if (
        not word
        or len(word) == 0
        or type(word) != str
    ):
        return False

    initial_word = word

    if len(word) == 1:
        return True

    final_word = "".join(reversing_word(list(word)))

    if final_word == initial_word:
        return True
    else:
        return False

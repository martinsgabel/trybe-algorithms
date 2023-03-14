def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return (first_string, second_string, False)

    first = "".join(string_sorting(list(first_string.lower())))
    second = "".join(string_sorting(list(second_string.lower())))

    if first == second:
        return (first, second, True)

    return (first, second, False)


def string_sorting(sentence, start=0, end=None):
    if end is None:
        end = len(sentence)
    if (end - start) > 1:
        mid = (start + end) // 2
        string_sorting(sentence, start, mid)
        string_sorting(sentence, mid, end)
        merge(sentence, start, mid, end)
    return sentence


def merge(sentence, start, mid, end):
    left = sentence[start:mid]
    right = sentence[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            sentence[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            sentence[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            sentence[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            sentence[general_index] = right[right_index]
            right_index = right_index + 1

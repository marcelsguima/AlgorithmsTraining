def is_anagram(first_string, second_string):
    word1 = "".join(merge(list(first_string.lower())))
    word2 = "".join(merge(list(second_string.lower())))
    if len(word1) == 0 or len(word2) == 0:
        return (word1, word2, False)
    true = (word1, word2, True)
    false = (word1, word2, False)
    return true if word1 == word2 else false


def merge(word):
    if len(word) <= 1:
        return word
    half_point = len(word) // 2
    right_word = merge(word[half_point:])
    left_word = merge(word[:half_point])
    return join(right_word, left_word)


def join(right_word, left_word):
    anagram = []
    while right_word and left_word:
        if left_word[0] < right_word[0]:
            anagram.append(left_word.pop(0))
        else:
            anagram.append(right_word.pop(0))
    anagram.extend(right_word)
    anagram.extend(left_word)
    return anagram

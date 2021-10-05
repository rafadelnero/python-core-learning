
# A Permutation of a string is another string that contains same characters,
# only the order of characters can be different. For example, “abcd” and “dabc” are
from re import split


def check_permutation(str1: str, str2: str):
    str1_array = list(str1)
    str2_array = list(str2)

    str1_array.sort()
    str2_array.sort()

    return str1_array == str2_array


def check_permutation_character_counts_book_solution(str1: str, str2: str):
    if len(str1) != len(str2):
        return False

    letters = [int]
    for i in range(128):
        letters.append(0)

    str1_array = list(str1)
    # Counting chars on each ASCII position - ord(char) returns the ASCII code
    for str1_char in str1_array:
        letters[ord(str1_char)] = letters[ord(str1_char)] + 1

    for i in range(len(str2)):
        str2_char = str2[i]
        letters[ord(str2_char)] = letters[ord(str2_char)] - 1

        if letters[ord(str2_char)] < 0:
            return False

    return True


if __name__ == '__main__':
    print(check_permutation("abcdefg", "ebcdagf"))
    print(check_permutation_character_counts_book_solution("abcdefg", "ebcdagf"))
    print(check_permutation_character_counts_book_solution("abcdefg", "ebcdagff"))

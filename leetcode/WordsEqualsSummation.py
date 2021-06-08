
ASCII_A_CODE = 97


def is_sum_equal(first_word: str, second_word: str, target_word: str):
    first_word_number = convert_string_to_number(first_word)
    second_word_number = convert_string_to_number(second_word)
    third_word_number = convert_string_to_number(target_word)

    return first_word_number + second_word_number == third_word_number


def convert_string_to_number(word):
    word_number = ""
    for letter in word:
        word_number += str(ord(letter) - ASCII_A_CODE)

    return int(word_number)


if __name__ == '__main__':
    result = is_sum_equal("acb", "cba", "cdb")
    print(result)

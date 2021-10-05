

def is_characters_unique(text: str) -> bool:
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                return False

    return True


def is_characters_unique_book_solution(text: str) -> bool:
    if len(text) > 128:
        return False

    char_set = [bool]
    for i in range(128):
        char_set.append(False)

    for i in range(len(text)):
        val = text[i]
        if char_set[ord(val)]:
            return False
        char_set[ord(val)] = True

    return True


if __name__ == '__main__':
    print(is_characters_unique("abcdefgh"))
    print(is_characters_unique_book_solution("abcdefgh"))

import re


def remove_vowels(word: str) -> str:
    return re.sub(r'[AEIOU]', '', word, flags=re.IGNORECASE)


if __name__ == '__main__':
    result = remove_vowels("leetcodeisacommunityforcoders")
    print(result)

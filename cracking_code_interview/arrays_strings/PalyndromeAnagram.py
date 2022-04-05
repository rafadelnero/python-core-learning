

def palindrome_anagram(text: str) -> bool:
    letters_count = [0] * 128
    text = text.lower()

    for letter in text:
        letters_count[ord(letter)] += 1

    odd_letter_count = 0
    even_letter_count = 0

    for letter_count in letters_count:
        if letter_count % 2 == 1:
            odd_letter_count += 1
        elif letter_count % 2 == 0:
            even_letter_count += 1

    return odd_letter_count > 1


if __name__ == '__main__':
    print(palindrome_anagram("Tact Coa"))

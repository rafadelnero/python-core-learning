

def is_palindrome(s: str) -> bool:
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]


def is_palindrome_recursion(s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True

    if s[0].lower() == s[len(s) - 1].lower():
        return is_palindrome_recursion(s[1:len(s) - 1])

    return False


if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))
    print(is_palindrome_recursion("Aibohphobia"))

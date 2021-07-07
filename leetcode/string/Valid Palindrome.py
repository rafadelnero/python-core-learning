

def is_palindrome(s: str) -> bool:
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]


if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))

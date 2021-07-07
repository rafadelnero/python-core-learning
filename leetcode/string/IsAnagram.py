from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for each_s in s:
        try:
            index = t.index(each_s)
            t = t[0: index:] + t[index + 1::]
        except Exception:
            return False

    return True


def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == '__main__':
    print(is_anagram("anagram", "nagaram"))
    print(is_anagram_counter("anagram", "nagaram"))

    my_str = "Welcome to Guru99 Tutorials!"
    print(Counter(my_str))
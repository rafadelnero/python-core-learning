import collections


def first_unique_char(s: str) -> int:
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i

    return -1


def first_unique_char_user_solution(s: str) -> int:
    """
    O(n) complexity
    """
    # build hash map : character and how often it appears
    count = collections.Counter(s)

    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


if __name__ == '__main__':
    print(first_unique_char("loveleetcode"))
    print(first_unique_char("aabb"))



def first_unique_char(s: str) -> int:
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i

    return -1


if __name__ == '__main__':
    print(first_unique_char("loveleetcode"))
    print(first_unique_char("aabb"))


def str_str_user_solution(a: str, ne: str) -> int:
    if ne in a:
        return a.index(ne)
    else:
        return -1


def str_str(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


if __name__ == '__main__':
    print(str_str("hello", "ll"))
    print(str_str_user_solution("hello", "ll"))

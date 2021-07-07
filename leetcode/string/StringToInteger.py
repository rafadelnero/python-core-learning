def atoi_user_solution(s: str) -> int:
    signs = {"+": 1, "-": -1}
    num, sign = 0, 0
    for i in range(len(s)):
        if s[i] == " " and not sign:
            continue
        if s[i] in signs and not sign:
            sign = signs[s[i]]
            continue
        if not s[i].isdigit():
            break
        num = 10 * num + ord(s[i]) - ord('0')
        if not sign:
            sign = 1
    num = min(2 ** 31, num)
    num *= sign
    return min(num, 2 ** 31 - 1)


def string_to_integer(s: str):
    s = s.strip()

    if s is None or len(s) < 1:
        return 0

    symbol = ""
    i = 0
    if s[i] in ("+", "-"):
        symbol = s[i]
        i += 1

    result = 0

    while i < len(s) and s[i].isdigit():
        result = result * 10 + (ord(s[i]) - ord("0"))
        i += 1

    if symbol == "-":
        result = -result

    max_signed_int = 2 ** 31 - 1
    min_signed_int = -2 ** 31

    if result > max_signed_int:
        return max_signed_int
    elif result < min_signed_int:
        return min_signed_int
    else:
        return result


if __name__ == '__main__':
    print(string_to_integer("44 rfdsafs"))
    print(string_to_integer("    -44"))
    print(string_to_integer("words and 987"))
    print(string_to_integer("-91283472332"))
    print(string_to_integer("91283472332"))
    print(string_to_integer("3.14159"))
    print(string_to_integer("-+12"))
    print(string_to_integer(""))
    print(string_to_integer("+"))
    print(string_to_integer("00000-42a1234"))

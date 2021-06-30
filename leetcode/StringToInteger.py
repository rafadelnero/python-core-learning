def string_to_integer(s: str):
    only_numbers = ""
    s = s.strip()
    for i in range(len(s)):
        if not s[i].isdigit() and s[i] not in ("+", "-"):
            return 0
        if s[i].isdigit():
            only_numbers += s[i]
        elif s[i] == "-" or s[i] == "+":
            if i > 0 and (s[i - 1] in ("+", "-")):
                return 0
            elif i == 0:
                only_numbers += s[i]
        elif not s[i].isdigit() and i == 0:
            return 0
        elif not s[i].isdigit() and only_numbers is not None:
            return only_numbers if only_numbers.isdigit() else 0

    try:
        converted_int_number = int(only_numbers)
    except Exception:
        return 0

    max_signed_int = 2 ** 31 - 1
    min_signed_int = -2 ** 31
    if only_numbers == "":
        return 0
    elif converted_int_number > max_signed_int:
        return max_signed_int
    elif converted_int_number < min_signed_int:
        return min_signed_int
    else:
        return converted_int_number


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

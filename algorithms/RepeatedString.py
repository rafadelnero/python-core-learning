

def repeated_string(s, n):
    """
    There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer,
    n, find and print the number of letter a's in the first  letters of the infinite string.

    The `//` operator returns the nearest division integer number.
    """
    if n % len(s) == 0:
        count_a_in_str = s.count("a") * (n // len(s))
    else:
        remainder_s_count = n % len(s)
        count_a_in_str = s.count("a") * int(n / len(s))

        for i in range(remainder_s_count):
            if s[i] == "a":
                count_a_in_str += 1

    print(count_a_in_str)


def repeated_string_user_solution(s, n):
    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))


if __name__ == "__main__":
    repeated_string("aba", 10)
    # repeated_string_user_solution("aba", 10)
    # repeated_string("abaaa", 17)
    # repeated_string("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm",
    #                  736778906400)# Expected output is 51574523448

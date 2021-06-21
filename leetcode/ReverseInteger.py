import sys


def reverse_integer(x: int) -> int:
    str_number = str(x)
    if "-" in str(str_number):
        reversed_str = "-" + str_number[:-len(str_number):-1]
    else:
        reversed_str = str_number[::-1]

    reversed_int = int(reversed_str)
    if abs(reversed_int) > (2 ** 31 - 1):
        return 0
    else:
        return reversed_int


def reverse_integer_pop(x: int):
    rev = 0
    while x != 0:
        pop = x % 10
        x /= 10
        if abs(rev) > (2 ** 31 - 1):
            return 0
    rev = rev * 10 + pop
    return rev


if __name__ == '__main__':
    print(reverse_integer(589))
    print(reverse_integer(-123))
    print(reverse_integer_pop(1534236469))

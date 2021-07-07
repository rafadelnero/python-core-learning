from typing import List


def reverse_string(s: List[str]) -> None:
    reverse_index = len(s) - 1
    for i in range(len(s) // 2):
        temp_letter = s[i]
        s[i] = s[reverse_index]
        s[reverse_index] = temp_letter
        reverse_index -= 1

    print(s)


def reverse_string_recursion(s):
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)
    print(s)


def reverse_string_pointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    print(s)


if __name__ == '__main__':
    # reverse_string(["H","a","n","n","a","h"])
    # reverse_string_recursion(["h", "e", "l", "l", "o"])
    reverse_string_pointer(["h", "e", "l", "l", "o"])

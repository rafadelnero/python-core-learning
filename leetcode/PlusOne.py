from typing import List


def plus_one(digits: List[int]) -> List[int]:
    digits_str = ""
    for digit in digits:
        digits_str += str(digit)

    return list(str(int(digits_str) + 1))


def plus_one_user_solution(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
            continue
        else:
            digits[i] += 1
            return digits

    digits.insert(0, 1)
    return digits


def plus_one_performant_solution(digits: List[int]) -> List[int]:
    # Last Bit
    LB = len(digits) - 1
    while digits[LB] == 9:
        digits[LB] = 0
        LB -= 1
    if LB == -1:  # extra digit req
        digits.insert(0, 1)
    else:
        digits[LB] = digits[LB] + 1
    return digits


if __name__ == '__main__':
    result = plus_one_user_solution([4, 3, 2, 1])
    print(result)

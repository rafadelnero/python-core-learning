
# 1 + 2 + 3 + 4 + 5 = 15 -- 3 + 6 + 10
def recursive_summation_from_bottom(input_numbers):
    if input_numbers >= 3:
        return input_numbers
    recursive_sum = input_numbers + recursive_summation_from_bottom(input_numbers + 1)
    return recursive_sum


def recursive_summation_from_top(input_numbers):
    if input_numbers <= 1:
        return input_numbers
    recursive_sum = input_numbers + recursive_summation_from_top(input_numbers - 1)
    return recursive_sum


if __name__ == '__main__':
    # result1 = recursive_summation_from_bottom(1)
    result2 = recursive_summation_from_top(3)
    # result2 = recursive_summation(10)
    # print(result1)
    print(result2)

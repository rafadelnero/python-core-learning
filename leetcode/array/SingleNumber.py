from typing import List


def single_number_optimized(nums: List[int]) -> int:
    c = 0
    for x in nums:
        c = c ^ x
    return c

# 0100
# 0001
# ----
# 0101 = 5

# 0101
# 0010 == 2
# ----
# 0111 == 7
# 0001 == 1
# -----
# 0110 == 6


def single_number(nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) == 1:
            return num

    return 0


if __name__ == '__main__':
    print(single_number_optimized([4, 1, 2, 1, 2]))
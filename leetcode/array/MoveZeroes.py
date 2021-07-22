from typing import List


def move_zeroes_optimized(nums: List[int]) -> None:
    i = 0
    zero_count = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            zero_count += 1
        else:
            i += 1
    complementary = [0] * zero_count
    nums.extend(complementary)


def move_zeroes(nums: List[int]) -> None:
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1

    for num in range(zero_count):
        nums.remove(0)
        nums.insert(len(nums), 0)


if __name__ == '__main__':
    list_zeroes = [0, 1, 0, 3, 12]
    move_zeroes_optimized(list_zeroes)
    print(list_zeroes)

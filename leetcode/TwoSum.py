from typing import List


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    indexes = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums), 1):
            two_sum_result = nums[i] + nums[j]
            indexes.append(i)
            indexes.append(j)
            if two_sum_result == target:
                return indexes
            else:
                indexes.clear()


def two_sum_dict(nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    for i in range(len(nums)):
        nums_dict[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_dict and nums_dict[complement] != i:
            return [i, nums_dict[complement]]


# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
if __name__ == '__main__':
    # print(two_sum_dict([2, 7, 11, 15], 9))
    print(two_sum_dict([3, 2, 9, 8, 4], 6))
    # print(two_sum_dict([3, 2, 4], 6))
    # print(two_sum_dict([3, 2, 3], 6))


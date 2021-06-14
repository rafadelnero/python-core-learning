from typing import List


def remove_duplicates(nums: List[int]) -> int:
    for i in range(len(nums) - 1, -1, -1):
        if nums.count(nums[i]) > 1:
            nums.remove(nums[i])

    return len(nums)


def remove_duplicates_user_solution(nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)


if __name__ == '__main__':
    # result = remove_duplicates([1, 1, 2])
    # result = remove_duplicates([1, 1, 1, 1])
    result = remove_duplicates_user_solution([1, 1, 1, 1])
    print(result)

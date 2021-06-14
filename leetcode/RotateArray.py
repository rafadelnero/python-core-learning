import collections
from typing import List


def rotate_deque(nums: List[int], k: int) -> None:
    deque_nums = collections.deque(nums)
    deque_nums.rotate(k)
    nums.clear()
    nums.extend(list(deque_nums))
    print(nums)


def rotate_list_not_performant(nums: List[int], k: int) -> None:
    while k > 0:
        nums[0], nums[len(nums) - 1] = nums[len(nums) - 1], nums[0]
        # Run the array in reverse until the position 1
        for i in range(len(nums) - 1, 1, -1):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        k -= 1
    print(nums)


def rotate_queue_optimized(nums: List[int], k: int) -> None:
    k = k % len(nums)
    k = len(nums) - k
    while k:
        elem = nums.pop(0)
        nums.append(elem)
        k -= 1

    print(nums)


if __name__ == '__main__':
    # rotate_list([1, 2, 3, 4, 5, 6, 7], 3)
    # rotate_deque([1, 2, 3, 4, 5, 6, 7], 3)
    rotate_queue_optimized([1, 2, 3, 4, 5, 6, 7], 3)


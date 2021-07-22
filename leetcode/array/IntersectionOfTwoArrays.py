import collections
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    intersected_array = []

    for num1 in nums1:
        if num1 in nums2:
            intersected_array.append(num1)
            nums2.remove(num1)

    return intersected_array


def intersect_performant_solution(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    counts = collections.defaultdict(int)
    for num in nums1:
        counts[num] += 1
    ret = []
    for num in nums2:
        if counts[num] > 0:
            ret.append(num)
            counts[num] -= 1
    return ret


if __name__ == '__main__':
    print(intersect([1, 2, 2, 1], [2]))

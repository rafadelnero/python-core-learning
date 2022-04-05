
# O(n)2
def two_number_sum(array, target_sum):
    array.sort()

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]
            elif array[i] > target_sum:
                return []

    return []


# O(n) time | O(n) space
def two_number_sum_dict(array, target_sum):
    nums = {}
    for num in array:
        potential_match = target_sum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return []


if __name__ == '__main__':
    # print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_number_sum_dict([3, 5, -4, 8, 11, 1, -1, 6], 10))
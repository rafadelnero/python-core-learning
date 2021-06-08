from typing import List


def running_sum(nums: []) -> []:
    """
       The goal of this algorithm is to sum the array elements as it goes. For example:
       Input: nums = [1,2,3,4]
       Output: [1,3,6,10]
       Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
       :param nums: an array of the length between 1 and 1000
       :return: the running sum of the arrays
    """
    # for with nums
    # for with nums until the current element and then sum the elements
    # Put the sum into a new array

    array_running_result = []
    array_running_sum = 0

    for number_index in range(len(nums)):
        for running_number_index in range(number_index + 1):
            array_running_sum += nums[running_number_index]

        array_running_result.append(array_running_sum)
        array_running_sum = 0

    return array_running_result


def running_sum_user_solution(nums: List[int]) -> List[int]:
    i = 0  # init to 0, to start from 0th index
    while i < len(nums):  # traverse the array till end
        if i != 0:
            # add previous values in the array and store in the current index
            #  skip 0th index because it is beginning of array, for eg: [1,2,3] -> 1)
            #  skip 0th index i.e value 1, then at index 1 arr[1] = arr1[1] + arr[0], i.e 3,
            #  now array becomes [1,3,3] and then in next iteration arr[2] = arr[2] + arr[1], i.e 6,
            #  thus array becomes -> [1,6,6]
            nums[i] += nums[i - 1]
        i = i + 1  # going to next index
    return nums


if __name__ == '__main__':
    result = running_sum_user_solution([1, 2, 3, 4, 5])
    # result = running_sum([1, 2, 3, 4])
    print(result)

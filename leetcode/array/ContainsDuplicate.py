from typing import List


def contains_duplicate_user_solution_92_ms(nums: List[int]) -> bool:
    my_set = set()
    for num in nums:
        if num not in my_set:
            my_set.add(num)
        elif num in my_set:
            return True
    return False


def contains_duplicate(nums: List[int]) -> bool:
    original_nums_size = len(nums)
    set_nums_size = len(set(nums))

    return original_nums_size != set_nums_size


if __name__ == '__main__':
    result = [1, 2, 3, 1]
    print(contains_duplicate(result))
    result = [1, 2, 3, 4]
    print(contains_duplicate(result))

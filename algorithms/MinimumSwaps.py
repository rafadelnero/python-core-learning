# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n]
# without any duplicates. You are allowed to swap any two elements.
# Find the minimum number of swaps required to sort the array in ascending order.
#
# Example

# Perform the following steps:
#
# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]

def minimum_swaps(arr, swaps=0):
    n = len(arr)
    # iterate over entire array
    for i in range(0, n):
        # Checks if the element of the array is not in the correct position by the index.
        # For example, the element "2" should be in the index position "1".
        while arr[i] != (i+1):
            print(i)
            # temp is the correct index of arr[i]
            current_index = arr[i]-1
            print('temp', current_index)
            # swap this with whatever element is where arr[current_index] is, this will
            # continue to swap until arr[i] == index+1
            arr[i], arr[current_index] = arr[current_index], arr[i]
            # increase swaps
            swaps += 1
            print(arr)
    return swaps


if __name__ == '__main__':
    swap_count = minimum_swaps([1, 3, 5, 2, 4, 6, 7])
    print(swap_count)

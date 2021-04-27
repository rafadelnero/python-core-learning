

def bubble_sort(arr):
    """
    The bubble method sorts the left most element and put it to the right most position.
      When the element is on the right, it's already sorted.
    """
    array_length = len(arr)

    # Traverse through all array elements
    for i in range(array_length):
        # Last i elements are already in place && don't check the already sorted part of the array
        for j in range(0, array_length - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    # Driver code to test above
    arr_param = [90, 64, 34, 25, 12, 22, 11]

    bubble_sort(arr_param)

    print("Sorted array is:")
    for i in range(len(arr_param)):
        print("%d" % arr_param[i])

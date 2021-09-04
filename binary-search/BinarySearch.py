
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def binary_search_recursive(arr, start, end, target):
    # Check base case
    if end >= start:

        mid = start + (end - start) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > target:
            return binary_search_recursive(arr, start, mid - 1, target)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, end, target)

    else:
        # Element is not present in the array
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    # result = binary_search(arr, x)
    result = binary_search_recursive(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

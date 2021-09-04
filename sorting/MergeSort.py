
# Python program for implementation of MergeSort - Big O(n * log n)
def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        left_array = arr[:mid]

        # into 2 halves
        right_array = arr[mid:]

        # Sorting the first half
        merge_sort(left_array)

        # Sorting the second half
        merge_sort(right_array)

        i = j = k = 0

        # Copy data to temp arrays left_array[] and right_array[]
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr_param = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print_list(arr_param)
    merge_sort(arr_param)
    print("Sorted array is: ", end="\n")
    print_list(arr_param)


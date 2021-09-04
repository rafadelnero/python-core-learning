

# Complexity Best Ω(n)	Average θ(n^2)	Worst O(n^2)

# Traverse array with index i
# set min_index to i
# Traverse through j and set min_index with j if array[j] is lower than array[i]
# Finally swap values out of the inner loop

# The selection sort selects the lowest number and swap it to most left position
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array), 1):
            if array[j] < array[i]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == '__main__':
    print(selection_sort([64, 22, 43, 90, 11]))
    print(selection_sort([90, 77, 43, 22, 11]))

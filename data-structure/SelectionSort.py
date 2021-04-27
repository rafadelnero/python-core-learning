
"""
PARAMETER	DESCRIPTION
start	(optional) Starting point of the sequence. It defaults to 0.
stop (required)	Endpoint of the sequence. This item will not be included in the sequence.
step (optional)	Step size of the sequence. It defaults to 1.
"""


def selection_sort(list):
    for i in range(len(list)):
        # this is the variable that will control the lowest number index.
        current_min_index = i

        # start loop, it doesn't go through what is already sorted in the beginning of the list.
        for j in range(current_min_index + 1, len(list)):
            # Checks what is the lowest number and then set the current_min_index.
            if list[j] < list[current_min_index]:
                print(j, i)
                current_min_index = j

            # If the index changed, swap the values
            if current_min_index != i:
                # if yes, switch the values in the list
                old_min_value = list[i]
                list[i], list[current_min_index] = list[current_min_index], old_min_value

    return list


if __name__ == '__main__':
    list_parameter = [23, 4, 42, 8, 16, 15]
    print(selection_sort(list_parameter))

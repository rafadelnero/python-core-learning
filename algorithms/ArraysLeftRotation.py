

# Complete the rotLeft function below.
def rotLeft(array, rotate_left_count):
    for i in range(rotate_left_count):
        array.append(array[0])
        del(array[0])

    return array


if __name__ == '__main__':
    array_left_rotation = rotLeft([1, 2, 3, 4, 5], 2)
    assert array_left_rotation == [3, 4, 5, 1, 2]


def mini_max_sum(array):
    array.sort()

    min_sum = array[0] + array[1] + array[2] + array[3]
    max_sum = array[1] + array[2] + array[3] + array[4]

    return f"{min_sum} {max_sum}"


if __name__ == '__main__':
    print(mini_max_sum([1, 2, 3, 4, 5]))
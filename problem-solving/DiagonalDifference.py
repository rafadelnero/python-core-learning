

def diagonal_difference(arr):
    left_to_right_diagonal = right_to_left_diagonal = 0

    left_index = 0
    right_index = len(arr) - 1
    for row in range(0, len(arr), 1):
        left_to_right_diagonal += arr[row][left_index]
        right_to_left_diagonal += arr[row][right_index]
        left_index += 1
        right_index -= 1

    return abs(left_to_right_diagonal - right_to_left_diagonal)


if __name__ == '__main__':
    result = diagonal_difference([[11, 2, 4],
                                  [4, 5, 6],
                                  [10, 8, -12]])
    print(result)

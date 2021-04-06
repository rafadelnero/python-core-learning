
def hourglass_sum(arr):
    """
    Hourglass example:
    a b c
      d
    e f g
    Sample Input
        1 1 1 0 0 0
        0 1 0 0 0 0
        1 1 1 0 0 0
        0 0 2 4 4 0
        0 0 0 2 0 0
        0 0 1 2 4 0

    Sample Output
        19
    """
    hourglass_total = []
    result = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if len(arr) - i >= 3 and len(arr[j]) - j >= 3:
                hourglass_total.append(sum_each_hourglass(arr, i, j, result))

    print(max(hourglass_total))


def sum_each_hourglass(arr, i, j, result):
    result += arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
    result += arr[i + 1][j + 1]
    result += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
    return result


def hourglass_user_solution(arr):
    hourglass_total_sum = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            hourglass_total_sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                                       arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])

    print(max(hourglass_total_sum))


if __name__ == '__main__':
    hourglass_sum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
                  [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])

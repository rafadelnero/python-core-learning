

def plus_minus(array):
    positive_ratio = 0
    negative_ratio = 0
    zero_ratio = 0

    for number in array:
        if number > 0:
            positive_ratio += 1
        elif number < 0:
            negative_ratio += 1
        else:
            zero_ratio += 1

    return "{:.6f}\n{:.6f}\n{:.6f}".format(positive_ratio / len(array),
                                           negative_ratio / len(array), zero_ratio / len(array))


if __name__ == '__main__':
    result = plus_minus([-4, 3, -9, 0, 4, 1])
    print(result)



def find_binary(decimal: int, result: str):
    if decimal == 0:
        return result

    result = decimal % 2 + result
    return find_binary(decimal // 2, result)


if __name__ == '__main__':
    find_binary(10, 3)
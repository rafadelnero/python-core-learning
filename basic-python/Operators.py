

if __name__ == '__main__':
    # ~ complements operator
    # Revert binary numbers - changes 0 to 1 or vice-versa
    # It's also useful to convert numbers to positive or negative
    # 12 == 00001100
    # 13 == 00001101
    print(~-12 + 1)
    print(~13 + 1)
    print(13 & 12)
    print(13 | 12)
    print(13 ^ 12)

    # & compares bit by bit with the "&" operator. 0 - 0 = 0 | 0 - 1 = 0 | 1 - 1 = 1
    # 00001100
    # 00001101
    # ________
    # 00001100 == 12

    # | compares bit by bit with the "|" operator. 0 - 0 = 0 | 0 - 1 = 1 | 1 - 1 = 1
    # 00001100
    # 00001101
    # ________
    # 00001101 == 13

    # ^ compares bit by bit with the "^" (xor) operator. 0 - 0 = 0 | 0 - 1 = 1 | 1 - 0 = 1 | 1 - 1 = 0
    # 00001100
    # 00001101
    # ________
    # 00000001 == 1

    # 11001
    # 11110
    # -----
    # 00111 == 7

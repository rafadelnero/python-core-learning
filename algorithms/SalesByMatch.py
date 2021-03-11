from collections import Counter


def sock_merchant(socks_quantity, socks):
    socks.sort()
    print(socks)

    pair_of_socks = 0
    found_pair = False

    for i in range(socks_quantity - 1):
        if found_pair:
            found_pair = False
            continue

        if socks[i] == socks[i + 1]:
            pair_of_socks += 1
            found_pair = True

    print("Result", pair_of_socks)
    return pair_of_socks


def sock_merchant_users_solution(socks_array):
    # Need to understand what is this Counter class
    socks, pairs = Counter(map(int, socks_array.strip().split())), 0
    for s in socks:
        pairs += socks[s] // 2
    print(pairs)


if __name__ == "__main__":
    sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    # sock_merchant_users_solution([10, 20, 20, 10, 10, 30, 50, 10, 20])

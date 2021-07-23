from typing import List


def get_max_profit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit


if __name__ == '__main__':
    print(get_max_profit([7, 1, 5, 3, 6, 4]))

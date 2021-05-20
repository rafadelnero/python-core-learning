

def birthday_cake_candles(candles):
    higher_candle = max(candles)
    return candles.count(higher_candle)


if __name__ == '__main__':
    print(birthday_cake_candles([3, 2, 1, 3]))
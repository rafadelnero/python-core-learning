
# 5 x 4 x 3 x 2 x 1 = 120
#   20    60    120
def factorial(n):
    if n == 0:
        print("After n == 0")
        return 1
    else:
        print("Preparing factorial:", n)
        factorial_result = n * factorial(n - 1)
        print("Invoking factorial:", factorial_result)
        return factorial_result


if __name__ == '__main__':
    result = factorial(5)
    print(result)

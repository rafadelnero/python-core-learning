

def fibonacci(n: int):
    a = 0
    b = 1
    for i in range(1, n):
        fibo_sum = a + b
        a = b
        b = fibo_sum

    return b


def fibonacci_recursion(n: int):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 0:
        return 0
        # Second Fibonacci number is 1
    elif n == 1:
        return 1
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)


if __name__ == '__main__':
    print(fibonacci_recursion(9))

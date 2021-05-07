

def staircase(n):
    for i in range(n):
        print(" " * (n - i - 1) + "#" * (i + 1))


def staircase_user_solution(n):
    for i in range(1, n + 1):
        # rjust adds padding to the string
        print(("#" * i).rjust(n))


if __name__ == '__main__':
    staircase(5)

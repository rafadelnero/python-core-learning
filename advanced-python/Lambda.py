# Lambda functions
# A lambda function is a small (one line) anonymous function that is defined without a name. A lambda function can take any number of arguments, but can only have one expression. While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

# `lambda arguments: expression`

# Lambda functions are used when a simple function is used only once or for a short period in your code. It's most common use is as an argument to higher-order functions (functions that takes in other functions as arguments). They are also used along with built-in functions like  `map()`, `filter()`, `reduce()`.


# a lambda function that multiplies two input arguments and returns the result
def multiply_2_numbers():
    f = lambda x, y: x * y
    val3 = f(2, 10)
    val4 = f(7, 5)
    print(val3, val4)


def sum_4_numbers():
    f = lambda r, x, y, z: r + x + y + z
    print(f(1, 2, 2, 3))


def simulate_java_predicate():
    f = lambda x, y: x and y
    print(f(True, False))


## Usage example: Lamdba inside another function
# Return a customized lambda function from another function and create different function variations depending on your needs.


def myfunc(n):
    return lambda x: x * n


def doubler_tripler_functions():
    doubler = myfunc(2)
    print(doubler(6))

    tripler = myfunc(3)
    print(tripler(6))


if __name__ == '__main__':
    doubler_tripler_functions()


## Custom sorting using a lambda function as key parameter
# The key function transforms each element before sorting.

def custom_lambda_sorting():
    points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
    sorted_by_y = sorted(points2D, key=lambda x: x[1])
    print(sorted_by_y)

    mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
    sorted_by_abs = sorted(mylist, key=lambda x: abs(x))
    print(sorted_by_abs)


## Use lambda for map function
# `map(func, seq)`, transforms each element with the function.

def using_map():
    a = [1, 2, 3, 4, 5, 6]
    b = list(map(lambda x: x * 2, a))

    # However, try to prefer list comprehension
    # Use map if you have an already defined function
    c = [x * 2 for x in a]
    print(b)
    print(c)


## Use lambda for filter function
# `filter(func, seq)`, returns all elements for which func evaluates to True.

def filter():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = list(filter(lambda x: (x % 2 == 0), a))

    # However, the same can be achieved with list comprehension
    c = [x for x in a if x % 2 == 0]
    print(b)
    print(c)


# reduce
# `reduce(func, seq)`, repeatedly applies the func to the elements and returns a single value.
# `func` takes 2 arguments.

def reduce_function():
    from functools import reduce
    a = [1, 2, 3, 4]
    product_a = reduce(lambda x, y: x * y, a)
    print(product_a)
    sum_a = reduce(lambda x, y: x + y, a)
    print(sum_a)


# a lambda function that adds 10 to the input argument
def add_10_lambda():
    f = lambda x: x + 10
    val1 = f(5)
    val2 = f(2)
    print(val1, val2)

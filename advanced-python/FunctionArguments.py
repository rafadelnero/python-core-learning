# Positional and keyword arguments


def foo(a, b, c):
    print(a, b, c)


def testing_arguments_positions():
    # positional arguments
    foo(1, 2, 3)

    # keyword arguments
    foo(a=1, b=2, c=3)
    foo(c=3, b=2, a=1)  # Note that the order is not important here

    # mix of both
    foo(1, b=2, c=3)

    # This is not allowed:
    # foo(1, b=2, 3) # positional argument after keyword argument
    foo(1, b=2, a=3) # multiple values for argument 'a'

# Default arguments


def foo(a, b, c, d=4):
    print(a, b, c, d)


foo(1, 2, 3, 4)
foo(1, b=2, c=3, d=100)

# not allowed: default arguments must be at the end
# def foo(a, b=2, c, d=4):
#     print(a, b, c, d)

## Variable-length arguments (`*args` and `**kwargs`)
# - If you mark a parameter with one asterisk (` * `), you can pass any number of positional arguments to your function (Typically called ` * args`)
# - If you mark a parameter with two asterisks (` ** `), you can pass any number of keyword arguments to this function (Typically called ` ** kwargs`).


def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])




# 3, 4, 5 are combined into args
# six and seven are combined into kwargs


if __name__ == '__main__':
    foo(1, 2, 3, 4, 5, six=6, seven=7)
    print()
    foo(1, 2, three=3)

# omitting of args or kwargs is also possible


def foo(a, b, *, c, d):
    print(a, b, c, d)


foo(1, 2, c=3, d=4)


# not allowed:
# foo(1, 2, 3, 4)

# arguments after variable-length arguments must be keyword arguments
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)


foo(8, 9, 10, last=50)


def foo(a, b, c):
    print(a, b, c)


# list/tuple unpacking, length must match
my_list = [4, 5, 6]  # or tuple
foo(*my_list)

# dict unpacking, keys and length must match
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

# my_dict = {'a': 1, 'b': 2, 'd': 3} # not possible since wrong keyword


def foo1():
    x = number  # global variable can only be accessed here
    print('number in function:', x)


number = 0
foo1()


# modifying the global variable
def foo2():
    global number  # global variable can now be accessed and modified
    number = 3
    print('number before foo2(): ', number)
    foo2()  # modifies the global variable
    print('number after foo2(): ', number)


number = 0


def foo3():
    number = 3  # this is a local variable
    print('number before foo3(): ', number)
    foo3()  # does not modify the global variable
    print('number after foo3(): ', number)

## Parameter passing
# Python uses a mechanism, which is known as "Call-by-Object" or "Call-by-Object-Reference. The following rules must be considered:
# - The parameter passed in is actually a reference to an object(but the reference is passed by value)
# - Difference between mutable and immutable data types
#
# This means that:

# 1. Mutable objects(e.g.lists, dict) can be changed within a method. *But if you
# rebind the reference in the method, the outer reference will still point at the
# original object.
# 3. Immutable objects(e.g.int, string) cannot be changed within a method. *But immutable object CONTAINED
# WITHIN a mutable object can be re - assigned within a method.


# immutable objects -> no change
def foo(x):
    x = 5  # x += 5 also no effect since x is immutable and a new variable must be created

    var = 10
    print('var before foo():', var)
    foo(var)
    print('var after foo():', var)


# mutable objects -> change
def foo(a_list):
    a_list.append(4)

    my_list = [1, 2, 3]
    print('my_list before foo():', my_list)
    foo(my_list)
    print('my_list after foo():', my_list)


# immutable objects within a mutable object -> change
def foo(a_list):
    a_list[0] = -100
    a_list[2] = "Paul"

    my_list = [1, 2, "Max"]
    print('my_list before foo():', my_list)
    foo(my_list)
    print('my_list after foo():', my_list)


# Rebind a mutable reference -> no change
def foo(a_list):
    a_list = [50, 60, 70]  # a_list is now a new local variable within the function
    a_list.append(50)
    my_list = [1, 2, 3]
    print('my_list before foo():', my_list)
    foo(my_list)
    print('my_list after foo():', my_list)

# Be careful with `+= ` and `=` operations for mutable types.
# The first operation has an effect on the passed argument while the latter has not:


# another example with rebinding references:
def foo(a_list):
    a_list += [4, 5]  # this chanches the outer variable


def bar(a_list):
    a_list = a_list + [4, 5]  # this rebinds the reference to a new local variable


def test_foo_list():
    my_list = [1, 2, 3]
    print('my_list before foo():', my_list)
    foo(my_list)
    print('my_list after foo():', my_list)

    my_list = [1, 2, 3]
    print('my_list before bar():', my_list)
    bar(my_list)
    print('my_list after bar():', my_list)
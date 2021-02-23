# Python Tricks
# Value swapping


def value_swap():
    a, b = 5, 10
    print(a, b)
    a, b = b, a
    print(a, b)
    # also possible in a list
    myList = [1, 2, 3, 4, 5]
    print("Initial list :", myList)
    myList[0], myList[1] = myList[1], myList[0]
    print("Modified list:", myList)

# Create a single string from list

def create_list_from_string():
    my_list = ["I", "am", "awesome"]

    # bad
    a = ""
    for i in my_list:
        a += i + " "
    print(a)

    # good
    a = " ".join(my_list)
    print(a)


# join method is much faster
def how_faster_is_join_method():
    from timeit import default_timer as timer
    my_list = ["a"] * 1000000
    print(my_list)

    # bad
    start = timer()
    a = ""
    for i in my_list:
        a += i
    end = timer()
    print(end - start)
    print(a)

    # good
    start = timer()
    a = " ".join(my_list)
    end = timer()
    print(end - start)
    #print(a)


if __name__ == '__main__':
    how_faster_is_join_method()
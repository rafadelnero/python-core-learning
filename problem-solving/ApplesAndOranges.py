

class TreeHouse:
    start_house_location: int
    end_house_location: int
    apple_tree_location: int
    orange_tree_location: int
    apples: []
    oranges: []

    def __init__(self, start_house_location, end_house_location, apple_tree_location, orange_tree_location,
                 apples, oranges):
        self.start_house_location = start_house_location
        self.end_house_location = end_house_location
        self.apple_tree_location = apple_tree_location
        self.orange_tree_location = orange_tree_location
        self.apples = apples
        self.oranges = oranges


def count_apples_and_oranges(tree_house: TreeHouse):
    apple_in_house = count_fruit_in_house(tree_house.apples, tree_house.apple_tree_location,
                                          tree_house.start_house_location, tree_house.end_house_location)

    orange_in_house = count_fruit_in_house(tree_house.oranges, tree_house.orange_tree_location,
                                           tree_house.start_house_location, tree_house.end_house_location)

    return apple_in_house, orange_in_house


def count_fruit_in_house(fruits, fruit_location, start_house_location, end_house_location):
    fruit_in_house = 0
    for i in range(len(fruits)):
        apple_location = fruit_location + fruits[i]
        if apple_location in range(start_house_location, end_house_location + 1):
            fruit_in_house += 1

    return fruit_in_house


if __name__ == '__main__':
    result = count_apples_and_oranges(TreeHouse(2, 3, 1, 5, [2], [-2]))
    print(result)


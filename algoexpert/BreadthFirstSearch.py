

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def breadth_first_search(self, array):
        queue = []
        queue.append(self)

        while len(queue) != 0:
            current_node = queue.pop(0)
            array.append(current_node.name)
            queue.extend(current_node.children)


if __name__ == '__main__':
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeA.children.append(nodeB)
    nodeA.children.append(nodeC)
    nodeA.children.append(nodeD)

    nodeE = Node("E")
    nodeB.children.append(nodeE)

    array = []
    nodeA.breadth_first_search(array)
    print(array)


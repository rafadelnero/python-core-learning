

class Node:
    def __init__(self, dataval=None):
        self.val = dataval
        self.next = None


class SLinkedList:
    node: Node

    def __init__(self):
        self.head = None

    def add_all(self, nodes: []):
        for index, node in enumerate(nodes):
            if self.head is None:
                self.head = nodes[index]

            if index < len(nodes) - 1:
                nodes[index].next = nodes[index + 1]

    def print_all(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def get_head(self):
        return self.head

def create_default_linked_list():
    linkedlist = SLinkedList()
    linkedlist.head = Node("4")
    e2 = Node("5")
    e3 = Node("1")
    e4 = Node("9")
    # Link first Node to second node
    linkedlist.head.next = e2

    # Link second Node to third node
    e2.next = e3
    e3.next = e4
    return linkedlist

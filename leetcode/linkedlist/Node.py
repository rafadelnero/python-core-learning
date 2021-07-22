

class SLinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, dataval=None):
        self.val = dataval
        self.next = None


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

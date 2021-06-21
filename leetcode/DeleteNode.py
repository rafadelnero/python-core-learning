

class Node:
    def __init__(self, dataval=None):
        self.val = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None


def delete_node(node: Node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    list1 = SLinkedList()
    list1.head = Node("4")
    e2 = Node("5")
    e3 = Node("1")
    e4 = Node("9")
    # Link first Node to second node
    list1.head.next = e2

    # Link second Node to third node
    e2.next = e3
    e3.next = e4

    delete_node(e2)

    printval = list1.head
    while printval is not None:
        print(printval.val)
        printval = printval.next



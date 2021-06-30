

class Node:
    def __init__(self, dataval=None):
        self.val = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None


def remove_nth_from_end(head: Node, n: int) -> Node:
    dummy = Node(-1)
    dummy.next = head
    slow = dummy
    fast = dummy

    while fast.next is not None:
        fast = fast.next
        if n <= 0:
            slow = slow.next
        n -= 1

    slow.next = slow.next.next

    return dummy.next


if __name__ == '__main__':
    list1 = SLinkedList()
    list1.head = Node("1")
    e2 = Node("2")
    e3 = Node("3")
    e4 = Node("4")
    e5 = Node("5")
    # Link first Node to second node
    list1.head.next = e2

    # Link second Node to third node
    e2.next = e3
    e3.next = e4
    e4.next = e5

    remove_nth_from_end(list1.head, 2)

    printval = list1.head
    while printval is not None:
        print(printval.val)
        printval = printval.next
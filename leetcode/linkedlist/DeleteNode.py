from leetcode.linkedlist.SLinkedList import ListNode, SLinkedList, create_default_linked_list


def delete_node(node: ListNode):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    list1 = create_default_linked_list()

    linkedlist = SLinkedList()
    linkedlist.head = ListNode("4")
    e2 = ListNode("5")
    e3 = ListNode("1")
    e4 = ListNode("9")
    # Link first Node to second node
    linkedlist.head.next = e2

    # Link second Node to third node
    e2.next = e3
    e3.next = e4

    delete_node(e3)

    printval = list1.head
    while printval is not None:
        print(printval.val)
        printval = printval.next



from leetcode.linkedlist.SLinkedList import ListNode, SLinkedList, create_default_linked_list


def delete_middle_node(head: ListNode) -> ListNode:
    node = head
    dict_nodes = {}
    i = 0

    while node:
        dict_nodes[i] = node
        node = node.next
        i = i + 1

    half_array = len(dict_nodes.values()) // 2

    node = head
    while node:
        if node.next == dict_nodes.get(half_array):
            node.next = node.next.next
            break
        node = node.next

    return head


if __name__ == '__main__':
    list1 = create_default_linked_list()

    linkedlist = SLinkedList()
    linkedlist.head = ListNode("1")
    e2 = ListNode("2")
    e3 = ListNode("3")
    e4 = ListNode("4")
    e5 = ListNode("5")
    e6 = ListNode("6")
    e7 = ListNode("7")
    e8 = ListNode("8")
    # Link first Node to second node
    linkedlist.head.next = e2

    # Link second Node to third node
    e2.next = e3
    e3.next = e4
    e4.next = e5
    e5.next = e6
    e6.next = e7
    e7.next = e8

    head = delete_middle_node(linkedlist.head)

    printval = head
    while printval is not None:
        print(printval.val)
        printval = printval.next



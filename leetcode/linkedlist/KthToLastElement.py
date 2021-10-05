from leetcode.linkedlist.SLinkedList import ListNode, SLinkedList, print_all_from_head, create_default_linked_list


def kth_to_last_element(head: ListNode, k: int) -> ListNode:
    node = head

    nodes_list = []
    while node:
        nodes_list.append(node)
        node = node.next

    return nodes_list[len(nodes_list) - k]


def kth_to_last_cracking_the_code_interview(head, k):
    runner = current = head
    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


if __name__ == '__main__':
    list1 = create_default_linked_list()

    linkedlist = SLinkedList()
    linkedlist.head = ListNode("4")
    e2 = ListNode("4")
    e3 = ListNode("4")
    e4 = ListNode("1")
    e5 = ListNode("9")
    e6 = ListNode("9")
    e7 = ListNode("2")
    # Link first Node to second node
    linkedlist.head.next = e2

    # Link second Node to third node
    e2.next = e3
    e3.next = e4
    e4.next = e5
    e5.next = e6
    e6.next = e7

    # kth_element = kth_to_last_element(linkedlist.head, 4)
    kth_element = kth_to_last_cracking_the_code_interview(linkedlist.head, 4)

    print(kth_element.val)


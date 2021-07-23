from leetcode.linkedlist.SLinkedList import Node, SLinkedList, create_default_linked_list


def merge_two_lists(l1: Node, l2: Node) -> Node:
    pass
    # while l1.next:


if __name__ == '__main__':
    linked_list1 = SLinkedList()
    linked_list1.add_all([Node("1"), Node("3"), Node("5"), Node("6")])

    linked_list2 = SLinkedList()
    linked_list2.add_all([Node("2"), Node("4"), Node("7"), Node("8")])

    merge_two_lists(linked_list1.head, linked_list2.head)

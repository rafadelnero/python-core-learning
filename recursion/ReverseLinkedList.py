from leetcode.linkedlist.SLinkedList import create_default_linked_list, print_all_from_head


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    node = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None

    return node


if __name__ == '__main__':
    head_param = create_default_linked_list().head
    print_all_from_head(head_param)
    result = reverse_linked_list(head_param)
    print_all_from_head(result)

from leetcode.linkedlist.SLinkedList import ListNode, SLinkedList, print_all_from_head


# https://www.youtube.com/watch?v=K63Mjf-H0B0&ab_channel=KevinNaughtonJr.
def merge_two_lists_user_solution(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    head = dummy
    while l1 and l2 is not None:
        if l1.val < l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next

    if l1 is not None:
        dummy.next = l1
    else:
        dummy.next = l2

    return head.next


if __name__ == '__main__':
    linked_list1 = SLinkedList()
    linked_list1.add_all([ListNode("1"), ListNode("3"), ListNode("5"), ListNode("6")])

    linked_list2 = SLinkedList()
    linked_list2.add_all([ListNode("2"), ListNode("4"), ListNode("7"), ListNode("8")])

    head = merge_two_lists_user_solution(linked_list1.head, linked_list2.head)

    print_all_from_head(head)

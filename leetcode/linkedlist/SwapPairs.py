from typing import Optional

from leetcode.linkedlist.SLinkedList import ListNode, SLinkedList, print_all_from_head


def swap_pairs_recursion(head: Optional[ListNode]) -> Optional[ListNode]:
    # If the list has no node or has only one node left.
    if not head or not head.next:
        return head

    # Nodes to be swapped
    first_node = head
    second_node = head.next

    # Swapping
    first_node.next = swap_pairs_recursion(second_node.next)
    second_node.next = first_node

    # Now the head is the second node
    return second_node


def swap_pairs_iterative(head: ListNode) -> ListNode:
    # Dummy node acts as the prevNode for the head node
    # of the list and hence stores pointer to the head node.
    dummy = ListNode(-1)
    dummy.next = head

    prev_node = dummy

    while head and head.next:
        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Reinitializing the head and prev_node for next swap
        prev_node = first_node
        head = first_node.next

    # Return the new head node.
    return dummy.next


if __name__ == '__main__':
    linked_list = SLinkedList()
    linked_list.add_all([ListNode("1"), ListNode("2"), ListNode("3"), ListNode("4"), ListNode("5")])
    # head = swap_pairs_iterative(linked_list.head)
    head = swap_pairs_recursion(linked_list.head)
    print_all_from_head(head)

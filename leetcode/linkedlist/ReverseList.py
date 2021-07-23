from leetcode.linkedlist.SLinkedList import Node, SLinkedList


def reverse_list_optimized(head: Node) -> Node:
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next  # Remember next node
        curr_node.next = prev_node  # REVERSE! None, first time round.
        prev_node = curr_node  # Used in the next iteration.
        curr_node = next_node  # Move to next node.
    head = prev_node
    return head

# 4 5 1 9
def reverse_list(head: Node) -> Node:
    current_node = head
    previous_node = None
    while current_node:
        next_node, current_node.next = current_node.next, previous_node
        previous_node, current_node = current_node, next_node
    head = previous_node
    return head


if __name__ == '__main__':
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
    head = reverse_list(linkedlist.head)

    printval = head
    while printval is not None:
        print(printval.val)
        printval = printval.next
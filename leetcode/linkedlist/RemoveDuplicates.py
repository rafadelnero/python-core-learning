from leetcode.linkedlist.SLinkedList import ListNode, SLinkedList, create_default_linked_list


def remove_duplicates(head: ListNode) -> ListNode:
    current = head
    previous = None
    seen = set()

    while current:
        if current.val in seen:
            previous.next = current.next
        else:
            seen.add(current.val)
            previous = current
        current = current.next

    return head

def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll


def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll


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

    head = remove_duplicates(linkedlist.head)

    printval = head
    while printval is not None:
        print(printval.val)
        printval = printval.next



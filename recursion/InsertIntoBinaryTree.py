from leetcode.linkedlist.SLinkedList import ListNode
from leetcode.tree.TreeNode import TreeNode, create_simple_sorted_bst_tree


def insert_node(head: TreeNode, data: int) -> TreeNode:
    if head is None:
        head = ListNode()
        head.val = data
        return head

    if head.val < data:
        head.right = insert_node(head.right, data)
    else:
        head.left = insert_node(head.left, data)
    return head


if __name__ == '__main__':
    tree_node = create_simple_sorted_bst_tree()
    head = insert_node(tree_node, 10)

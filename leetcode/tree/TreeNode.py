

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_two_levels_tree() -> TreeNode:
    second_node = TreeNode(20, None, None)
    root_node = TreeNode(3, None, second_node)
    return root_node


def create_simple_sorted_bst_tree() -> TreeNode:
    left_node = TreeNode(1, None, None)
    right_node = TreeNode(3, None, None)
    root_node = TreeNode(2, left_node, right_node)
    return root_node

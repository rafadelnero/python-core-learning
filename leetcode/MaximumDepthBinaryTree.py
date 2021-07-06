

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_stack_iteration(root: TreeNode):
    stack = []
    if root is not None:
        stack.append((1, root))

    depth = 0
    while stack:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))

    return depth


def max_depth_recursion(root):
    if root is None:
        return 0
    else:
        left_height = max_depth_recursion(root.left)
        right_height = max_depth_recursion(root.right)
        return max(left_height, right_height) + 1


if __name__ == '__main__':
    second_node = TreeNode(20, 15, 7)
    root_node = TreeNode(3, 9, second_node)
    print(max_depth_stack_iteration(root_node))
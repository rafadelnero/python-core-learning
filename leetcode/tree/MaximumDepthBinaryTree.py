from leetcode.tree.TreeNode import TreeNode, create_two_levels_tree


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
        print(root.val)
        right_height = max_depth_recursion(root.right)
        print(root.val)
        return max(left_height, right_height) + 1


def max_depth_optimal_solution(root):
    counter = 0
    height = 0

    if not root:
        return 0

    q = [root]

    while q:
        height += 1
        temp = []
        for i in q:
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        q = temp

    return height


if __name__ == '__main__':
    print(max_depth_recursion(create_two_levels_tree()))

    # 3
    #     20

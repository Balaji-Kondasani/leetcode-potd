# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            """
            Returns:
                (depth, subtree_root)
            depth = max depth from this node down to deepest leaf
            subtree_root = the node which is the smallest subtree containing all deepest leaves
            """
            if not node:
                return (0, None)

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            # If both sides have same depth, current node is LCA of deepest leaves
            if left_depth == right_depth:
                return (left_depth + 1, node)

            # If left deeper, answer comes from left subtree
            if left_depth > right_depth:
                return (left_depth + 1, left_node)

            # If right deeper, answer comes from right subtree
            return (right_depth + 1, right_node)

        return dfs(root)[1]

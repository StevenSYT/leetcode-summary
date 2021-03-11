# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode',
                             nodes: 'List[TreeNode]') -> 'TreeNode':
        p = nodes[0]
        if len(nodes) == 1:
            return p

        i = 1
        while i < len(nodes):
            q = nodes[i]
            p = self.lowestCommonAncestorForTwo(root, p, q)
            i += 1

        return p

    def lowestCommonAncestorForTwo(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestorForTwo(root.left, p, q)
        right = self.lowestCommonAncestorForTwo(root.right, p, q)

        if left and right:
            return root

        elif left:
            return left

        else:
            return right
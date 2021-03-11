# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        lca = self.findLCA(root, p, q)
        print(lca.val)
        if lca.val == p or lca.val == q:
            return abs(self.findLevel(root, p) - self.findLevel(root, q))

        else:
            return self.findLevel(root, p) + self.findLevel(
                root, q) - self.findLevel(root, lca.val) * 2

    def findLCA(self, root, p, q):
        if not root or root.val == p or root.val == q:
            return root

        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)

        if left and right:
            return root

        elif left:
            return left

        else:
            return right

    def findLevel(self, root, val):
        if not root:
            return None

        if root.val == val:
            return 1

        left_res = self.findLevel(root.left, val)
        right_res = self.findLevel(root.right, val)

        if left_res:
            return left_res + 1

        elif right_res:
            return right_res + 1

        else:
            return None

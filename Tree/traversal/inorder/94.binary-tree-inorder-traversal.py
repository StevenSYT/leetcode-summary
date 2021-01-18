#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return None
        res = []
        left = self.inorderTraversal(root.left)
        if left:
            res += left
        res.append(root.val)
        right = self.inorderTraversal(root.right)
        if right:
            res += right
        return res

# @lc code=end


#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i = 0
        self.res = []
        return self.res if self.dfs(root, voyage) else [-1]
        
        
    def dfs(self, root, voyage):
        if not root:
            return True
        
        if root.val != voyage[self.i]:
            return False

        self.i += 1

        if root.left and root.left.val != voyage[self.i]:
            self.res.append(root.val)
            return self.dfs(root.right, voyage) and self.dfs(root.left, voyage)

        else:
            return self.dfs(root.left, voyage) and self.dfs(root.right, voyage)
# @lc code=end


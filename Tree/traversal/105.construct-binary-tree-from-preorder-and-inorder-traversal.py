#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}
        preorder = deque(preorder)

        def helper(start, end):
            if start > end:
                return None

            cur_node = TreeNode(preorder.popleft())
            idx = inorder_dict[cur_node.val]
            cur_node.left = helper(start, idx - 1)
            cur_node.right = helper(idx + 1, end)

            return cur_node

        return helper(0, len(inorder) - 1)


# @lc code=end

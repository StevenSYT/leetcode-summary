#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}

        def helper(start, end):
            if start > end:
                return None

            cur_node = TreeNode(postorder.pop())
            idx = inorder_dict[cur_node.val]
            cur_node.right = helper(idx + 1, end)
            cur_node.left = helper(start, idx - 1)

            return cur_node

        return helper(0, len(inorder) - 1)


# @lc code=end

#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#


# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        for node in preorder.split(","):
            if slots == 0:
                return False

            if node == "#":
                slots -= 1

            else:
                slots += 1

        return slots == 0


# @lc code=end

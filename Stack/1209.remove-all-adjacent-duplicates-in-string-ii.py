#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:

            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
            while stack and stack[-1][1] == k:
                stack.pop()
        return ''.join(map(lambda x : x[0] * x[1], stack))
        
# @lc code=end


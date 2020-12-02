#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        top = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[top]:
                stack.pop()
                top += 1
        return not stack
# @lc code=end


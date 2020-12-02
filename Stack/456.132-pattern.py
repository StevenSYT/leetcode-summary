#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#


# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        mins = [float('inf')] * n
        for i in range(1, n):
            mins[i] = min(mins[i - 1], nums[i - 1])
        stack = []
        for j in range(n - 1, -1, -1):
            last = float('-inf')
            while stack and stack[-1] < nums[j]:
                last = stack.pop()
            # This if statement has two meanings:
            # 1. nums[j] was larger than the top of the stack
            # before the while loop, hence nums[j] can be a
            # candidate as the middle number of the '132 pattern'.
            # 2. The value of the last is the closest value to
            # nums[j] on the right hand side of nums[j]. And it is larger
            # than the smallest value one the left hand side of nums[j].
            # With these information, we know we found a '132 pattern'.
            if last > mins[j]:
                return True

            # At this point, we have nums[j] <= stack[-1], the values that
            # are popped in the process are thrown away because we don't
            # need them anymore (They are smaller than the minimum values
            # on left of nums[j]). Or we have an empty stack. In any of the
            # cases we listed, we need to push nums[j] to stack.
            stack.append(nums[j])
        return False


# @lc code=end

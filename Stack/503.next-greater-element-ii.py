#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
# 如果是circular list就连续遍历两遍，用一个stack。TC: O(N) SC: O(N)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        greater_list = [-1] * n
        stack = []
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                greater_list[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return greater_list
# @lc code=end


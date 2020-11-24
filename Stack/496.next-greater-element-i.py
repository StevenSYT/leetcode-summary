#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num_map = {}
        for num in nums2:
            while stack and stack[-1] < num:
                num_map[stack.pop()] = num
            stack.append(num)
        while stack:
            num_map[stack.pop()] = -1
        return map(lambda x : num_map[x], nums1)

# @lc code=end


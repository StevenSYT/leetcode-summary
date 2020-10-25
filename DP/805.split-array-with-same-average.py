#
# @lc app=leetcode id=805 lang=python3
#
# [805] Split Array With Same Average
#

# @lc code=start
class Solution:
    def splitArraySameAverageSolution1(self, A: List[int]) -> bool:
        s = sum(A)
        self.cache = {}
        for size in range(1, len(A) // 2 + 1):
            if (s * size % len(A) == 0): # Make sure the target is int
                if (self.dfs(s * size // len(A), size, tuple(A))):
                    return True
        return False
    def dfs(self, target, size, nums):
        if size == 0:
            return target == 0
        if (size > len(nums) or not nums):
            return False
        if ((target, size, nums) in self.cache):
            return self.cache[(target, size, nums)]
        res = any([
            self.dfs(target - nums[0], size - 1, nums[1:]),
            self.dfs(target, size, nums[1:])
        ])
        self.cache[(target, size, nums)] = res
        return res
    

    def splitArraySameAverage(self, A):
        A.sort(reverse=True)
        dp = {0:0}
        l, s = len(A), sum(A)
        for num in A:
            for k in sorted(dp.keys(), reverse=True):
                dp[k + num] = dp[k]+1
                k += num
                v = dp[k]
                if v and l - v and k * (l - v) == (s - k) * v:
                    return True
        return False 


        
# @lc code=end


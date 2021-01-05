#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#

# @lc code=start
from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums
        n = len(nums)
        score = [0] * n
        q = deque([nums[0]])
        
        for r in range(1, n):
            score[r] = max(score[q[0]], 0) + nums[r] 
            while q and r - q[0] >= k:
                q.popleft()
            while q and score[q[-1]] < score[r]:
                q.pop()
            q.append(r)
        return max(score[1:])
# @lc code=end


#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = min(bloomDay), max(bloomDay)
        res = -1

        while low <= high:
            mid = (low + high) // 2
            if self.canMake(bloomDay, m, k, mid):
                res = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        return res 
    
    def canMake(self, bloomDay, m, k, mid):
        cum_sum = 0
        num_b = 0

        for bloom in bloomDay:
            if bloom <= mid:
                # is available
                cum_sum += 1
            
            else:
                cum_sum = 0
            
            if cum_sum == k:
                num_b += 1
                cum_sum = 0
            
        return num_b >= m
# @lc code=end


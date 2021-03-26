#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]
                customers[i] = 0
        
        max_satisfied = cur_satisifed = satisfied

        for r in range(len(grumpy)):
            cur_satisifed += customers[r]

            if r >= X:
                cur_satisifed -= customers[r - X]
            
            max_satisfied = max(max_satisfied, cur_satisifed)
        
        return max_satisfied
# @lc code=end


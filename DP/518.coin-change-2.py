#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    # DFS will take up too much time
        dp = [1] + [0] * amount  # dp[n] = number of combinations to get n

        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] = dp[j] + dp[j - i]
        return dp[amount]
        
# @lc code=end


#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        if s == '': return 0
        
        new_s = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]: continue
            new_s += s[i]
        
        n = len(new_s)
        dp = [[float('inf')] * n for _ in range(n)]
        # dp[left][right]: 在这个区间内print最少的次数
        # dp[left][right]: 如果找到一个k，new_s[right] == new_s[k], 假设一定有这么一次print，就是从k到right，
        # 这样的话最后一个字符串就不用考虑了，因为在print [left, k] 的时候，只要某次print了new_s[k]，就可以顺便把
        # new_s[right]也打印了。如此一来dp[left][right] = dp[left][k] + dp[k+1][right - 1], 右边的substring就
        # 可以少考虑一个字符串。
        # 
        
        for i in range(0, n):
            dp[i][i] = 1
            if i < n - 1:
                dp[i][i+1] = 2
        
        for d in range(1, n):
            for left in range(0, n-d):
                right = left + d
                
                # worst case: print [left, right - 1], then print the right most char.
                dp[left][right] = 1 + dp[left][right - 1]
                for k in range(left, right):
                    if new_s[k] == new_s[right]:
                        dp[left][right] = min(dp[left][right], dp[left][k] + dp[k+1][right - 1])
        
        return dp[0][n-1]
        
# @lc code=end


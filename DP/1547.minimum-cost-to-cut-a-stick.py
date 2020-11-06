#
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#

# @lc code=start
class Solution:
    # 这道题要结合312. Burst Balloons 和 1039. Minimum Score Triangulation of Polygon
    # 来一起复习。
    # 这类问题感觉就是循环的时候，先定左右距离d，把d按增序循环，放在最外层循环，然后left就从0开始直到length - d，
    # 这样就有一个buttom up了。
    
    # 循环的body就是，选一个中间点作为分界，这个中间点的理解：
    # 1. 这道题是选一个cut，然后化为左右子问题. 
    # 2. Burst Balloons是选一个气球作为最后一个爆的气球，然后化为左右子问题.
    # 3. Minimum Score Triangulation of Polygon是，选一个中间的三角形作为最后结果中的一个三角形，然后化为左右子问题。 
    # 关键就是中间这个k以及其对应的值的含义。
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted([0] + cuts + [n])
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]
        for d in range(2, m):
            for i in range(0, m - d):
                j = i + d
                dp[i][j] = min([dp[i][k] + dp[k][j] for k in range(i+1, j)]) + cuts[j] - cuts[i]
        return dp[0][m-1]
        
# @lc code=end


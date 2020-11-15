#
# @lc app=leetcode id=1494 lang=python3
#
# [1494] Parallel Courses II
#


# @lc code=start
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]],
                             k: int) -> int:
        # '1111' -> 所有的课上完了
        # '0000' -> 一门都没上
        N = 1 << n
        dp = [float('inf')] * N

        # dp[state]: 当达到state的时候，最少需要多少学期
        dp[0] = 0

        # pres[i]: 第i门课的先修课有哪些
        pres = [0] * n
        for dep in dependencies:
            pres[dep[1] - 1] += (1 << (dep[0] - 1))

        # 有效的状态一定是递增
        for cur_state in range(N):
            if dp[cur_state] == float('inf'): continue
            can_study = 0
            for subject in range(n):
                if not (cur_state >> subject) & 1: continue
                if (cur_state & pres[subject]) == pres[subject]:
                    can_study |= (1 << subject)
            if bin(can_study).count('1') <= k:
                dp[can_study | cur_state] = min(dp[can_study | cur_state],
                                                dp[cur_state] + 1)
            else:
                sub = can_study
                while sub > 0:
                    if (bin(sub).count('1') <= k):
                        dp[sub | cur_state] = min(dp[sub | cur_state],
                                                  dp[cur_state] + 1)
                    sub = ((sub - 1) & can_study)  # 从can_study遍历一遍所有的子集，这个操作可以记住
        return dp[N - 1]


# @lc code=end

#
# @lc app=leetcode id=943 lang=python3
#
# [943] Find the Shortest Superstring
#


# @lc code=start
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        N = len(A)
        M = (1 << N)

        def distance(a, b):
            for i in range(min(len(a), len(b)), 0, -1):
                if a[-i:] == b[:i]:
                    return len(b) - i
            return len(b)

        def combine(a, b):
            for i in range(min(len(a), len(b)), 0, -1):
                if a[-i:] == b[:i]:
                    return a + b[i:]
            return a + b

        # 这是一道旅行商问题TSP(Traveling Salesman Problem)。
        # 对于两个string S1, S2, S1 -> S2的距离指的是从S1加多少个char，这个结果的string就包含S2了。
        # 假设有string A='abc', B='bcd', C='cde', 那么 A -> B = 1 因为A再加一个char 'd'就能包含B了，
        # 同理有： B -> C = 1, A -> C = 2, B -> A = 3, C -> A = 3, C -> B = 3.
        # dp[status][last]： 当前状态为status并且最后一个访问的city是last，存的值为当前的最优super string
        dp = [[float('inf')] * N for _ in range(M)]
        parent = [[-1] * N for _ in range(M)]
        dis = [[0] * N for _ in range(N)]

        # Get distances
        for i in range(N):
            for j in range(N):
                if i != j:
                    dis[i][j] = distance(A[i], A[j])
        # Base cases: if start with string i, the super string is i itself.
        for i in range(N):
            dp[1 << i][i] = len(A[i])

        # 状态转移：dp[status][last] = dp[status - last] + dis[sec_last][last] 选一个sec_last使行走的distance最小
        for status in range(M):
            for last in range(N):
                if (status & (1 << last)) == 0: continue
                prev_status = status ^ (1 << last)
                if prev_status == 0: continue
                for sec_last in range(N):
                    if (prev_status & (1 << sec_last)) == 0: continue
                    # Choose from the second last node to go from.
                    if dp[status][last] > dp[prev_status][sec_last] + dis[
                            sec_last][last]:

                        dp[status][last] = dp[prev_status][sec_last] + dis[
                            sec_last][last]
                        parent[status][last] = sec_last
        start = min(enumerate(dp[M - 1]), key=lambda x: x[1])[0]
        path = deque([start])

        status = M - 1
        while parent[status][start] != -1:
            prev = parent[status][start]
            path.appendleft(prev)
            status -= (1 << start)
            start = prev
        res = A[start]
        for i in range(1, len(path)):
            res = combine(res, A[path[i]])
        return res


# @lc code=end

#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        S = [0] * (N + 1)
        for i in range(N):
            S[i + 1] = S[i] + A[i]
        q = deque()

        # If res never changed, that means there was no valid
        # subarray. But if there is any valid subarray, the 
        # width would be smaller than N + 1
        res = N + 1
        for i in range(len(S)):
            while q and S[i] - S[q[0]] >= K:
                res = min(res, i - q.popleft())
            while q and S[i] <= S[q[-1]]:
                q.pop()
            q.append(i)
        return res if res < N + 1 else -1

# @lc code=end


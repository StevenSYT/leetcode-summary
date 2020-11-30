#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 not in arr:
            return False
        q = deque([start])
        n = len(arr)
        seen = set()
        while q:
            cur_idx = q.popleft()
            if cur_idx in seen: continue
            if arr[cur_idx] == 0:
                return True
            for next_idx in [cur_idx + arr[cur_idx], cur_idx - arr[cur_idx]]:
                if 0 <= next_idx < n:
                    q.append(next_idx)
            seen.add(cur_idx)
        return False


# @lc code=end

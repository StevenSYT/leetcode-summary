#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        val_to_pos = defaultdict(list)
        visited_pos = set()

        for pos, val in enumerate(arr):
            val_to_pos[val].append(pos)

        q = deque([(0, 0)])

        while q:
            step, pos = q.popleft()

            if pos == n - 1:
                return step

            if pos in visited_pos:
                continue

            visited_pos.add(pos)

            next_nodes = [pos + 1, pos - 1]
            while val_to_pos[arr[pos]]:
                next_pos = val_to_pos[arr[pos]].pop()
                if next_pos != pos:
                    next_nodes.append(next_pos)

            for p in next_nodes:
                if 0 <= p < n:
                    q.append((step + 1, p))


# @lc code=end

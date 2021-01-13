#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq


class Solution:
    # heapq based search. O(N^2*logN)
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [(grid[0][0], 0, 0)]
        heapq.heapify(q)
        n, res, visited = len(grid), 0, {(0, 0)}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while True:
            T, x, y = heapq.heappop(q)
            res = max(T, res)
            if x == y == n - 1:
                return res
            for nx, ny in map(lambda d: (x + d[0], y + d[1]), directions):
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(q, (grid[nx][ny], nx, ny))
                    visited.add((nx, ny))


# @lc code=end

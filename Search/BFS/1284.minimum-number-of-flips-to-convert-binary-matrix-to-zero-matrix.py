#
# @lc app=leetcode id=1284 lang=python3
#
# [1284] Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
#

# @lc code=start
from collections import deque


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        directions = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]

        # Construct initial state "start"
        start = 0
        for i in range(m):
            for j in range(n):
                start |= mat[i][j] << (i * n + j)

        q = deque([(0, start)])
        visited = set()

        while q:
            step, status = q.popleft()

            if not status:
                return step

            if status in visited:
                continue

            visited.add(status)

            for i in range(m):
                for j in range(n):
                    next_status = status

                    # Compute the next_status for a "flip"
                    for d in directions:
                        nx, ny = i + d[0], j + d[1]

                        if 0 <= nx < m and 0 <= ny < n:
                            next_status ^= 1 << (nx * n + ny)

                    q.append((step + 1, next_status))

        return -1


# @lc code=end

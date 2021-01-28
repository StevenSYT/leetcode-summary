#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m, n = len(matrix), len(matrix[0])

        pacific = [[0] * n for _ in range(m)]
        atlantic = [[0] * n for _ in range(m)]

        for i in range(m):
            self.bfs(i, 0, pacific, matrix)
            self.bfs(i, n - 1, atlantic, matrix)

        for j in range(n):
            self.bfs(0, j, pacific, matrix)
            self.bfs(m - 1, j, atlantic, matrix)

        res = []
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] == pacific[i][j] == 1:
                    res.append([i, j])
        return res

    def bfs(self, x, y, ocean, matrix):
        m, n = len(matrix), len(matrix[0])
        q = deque([(x, y)])

        while q:
            r, c = q.popleft()

            if ocean[r][c] == 1:
                continue

            ocean[r][c] = 1

            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + i, c + j
                # 从边界往内搜索，所以这里matrix[nr][nc] >= matrix[r][c]恰好跟条件相反
                if 0 <= nr < m and 0 <= nc < n:
                    if matrix[nr][nc] >= matrix[r][c]:
                        q.append((nr, nc))


# @lc code=end

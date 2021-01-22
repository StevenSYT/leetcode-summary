#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start
from collections import deque
import heapq


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        trees = []
        heapq.heapify(trees)

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(trees, (forest[i][j], i, j))

        cur = (0, 0)
        res = 0

        # 尝试把所有的tree按顺序砍掉
        while trees:
            h, x, y = heapq.heappop(trees)

            offset = self.distance(cur, x, y, forest)

            if offset == -1:
                return -1

            res += offset
            cur = (x, y)

        return res

    # BFS用来计算当前node到target tree的距离
    def distance(self, cur, x, y, forest):
        m, n = len(forest), len(forest[0])
        q = deque([(0, cur)])
        visited = set()

        while q:
            step, cur = q.popleft()

            if cur == (x, y):
                return step

            if cur in visited:
                continue

            visited.add(cur)

            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = cur[0] + d[0], cur[1] + d[1]

                if 0 <= nx < m and 0 <= ny < n and forest[nx][ny] >= 1 and (
                        nx, ny) not in visited:
                    q.append((step + 1, (nx, ny)))

        return -1


# @lc code=end

#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = set()
        # An element in the heap is a tuple of (h, x, y)
        # where h is the current water level for (x, y)
        # and x, y denote the position.
        heap = []
        heapq.heapify(heap)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Add left and right boundary to PQ
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            visited.add((i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited.add((i, n - 1))

        # Add top and bottom boundary to PQ
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            visited.add((0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited.add((m - 1, j))

        res = 0

        while heap:
            h, x, y = heapq.heappop(heap)

            for d in directions:
                nx, ny = x + d[0], y + d[1]

                if (nx, ny) in visited: continue

                if 0 <= nx < m and 0 <= ny < n:
                    if heightMap[nx][ny] < h:
                        res += h - heightMap[nx][ny]
                        heapq.heappush(heap, (h, nx, ny))
                    else:
                        heapq.heappush(heap, (heightMap[nx][ny], nx, ny))
                    visited.add((nx, ny))
        return res


# @lc code=end

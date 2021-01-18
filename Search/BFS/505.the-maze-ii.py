import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int],
                         destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = [(0, start[0], start[1])]
        heapq.heapify(q)

        visited = set()

        while q:
            steps, x, y = heapq.heappop(q)

            if [x, y] == destination:
                return steps

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for i, j in directions:
                next_steps = steps
                nx, ny = x, y

                while 0 <= nx + i < m and 0 <= ny + j < n and maze[nx + i][
                        ny + j] != 1:
                    nx, ny = nx + i, ny + j
                    next_steps += 1

                heapq.heappush(q, (next_steps, nx, ny))

        return -1
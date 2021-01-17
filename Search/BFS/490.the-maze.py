from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        q = deque([start])
        visited = set(tuple(start))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            pos = q.popleft()
            if pos == destination:
                return True
            for d in directions:
                x, y = pos[0], pos[1]
                nx, ny = x + d[0], y + d[1]
                
                # Move until hit a wall.
                # maintaining x, y ,nx, ny so that when while loop finished,
                # x, y is at the right spot where it is next to the wall.
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != 1:
                    x, y = nx, ny
                    nx, ny = nx + d[0], ny + d[1]
                if (x, y) not in visited:
                    q.append([x, y])
                    visited.add((x, y))
        return False
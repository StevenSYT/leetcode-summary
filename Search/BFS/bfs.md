# BFS

- [Is Graph Bipartite?](#is-graph-bipartite?)
- [Swim in Rising Water](#swim-in-rising-water)
- [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
- [Jump Game III](#jump-game-iii)
- [Open the Lock](#open-the-lock)
- [The Maze](#the-maze)
- [The Maze II](#the-maze-ii)
- [Trapping Rain Water II](#trapping-rain-water-ii)

## Is Graph Bipartite?

[785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)

**Solution**

这题 BFS 和 DFS 都能解，BFS 不太好想的地方是，初始不能只从一个点搜索就完了，要对每个点做一次 BFS。
一般惯性思维 BFS 从一个点开始就能搜完，其实会出现有的点从头到尾没有被搜到过。
DFS 经常会遇到对每个点做 DFS，比如 number of island。

解题思路就是要用一个数据结构将两种点“着色”，用两种“颜色”区分开。在搜索的时候相邻点着反色，
如果遇到已着色点，看见颜色冲突，就返回 False。如果全程无 False，就是返回 True。

BFS:

```python
# BFS
form collections import deque
def isBipartite1(self, graph: List[List[int]]) -> bool:
    nodes = {}
    for i in range(len(graph)):
        if i in nodes:
            continue
        q = deque([i])
        nodes[i] = 1

        while q:
            node = q.popleft()
            sign = nodes[node]
            for next_node in graph[node]:
                if next_node in nodes:
                    if nodes[next_node] == sign:
                        return False
                else:
                    nodes[next_node] = -sign
                    q.append(next_node)
    return True
```

DFS:

```python
def isBipartite(self, graph: List[List[int]]) -> bool:
    nodes = {}
    for i in range(len(graph)):
        if i not in nodes:
            nodes[i] = 1
            res = self.dfs(i, graph, nodes)
            if not res:
                return False
    return True

def dfs(self, node, graph, nodes):
    for next_node in graph[node]:
        if next_node in nodes:
            if nodes[next_node] == nodes[node]:
                return False
        else:
            nodes[next_node] = -nodes[node]
            res = self.dfs(next_node, graph, nodes)
            if res == False:
                return False
    return True
```

## Swim in Rising Water

[778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

**Solution**

这题有至少三种解法：DFS, Union-Find, 最优解是 PriorityQueue based search。
后续会把 DFS 和并查集的解法补上。

**Priority Queue:**

```python
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
```

## Cheapest Flights Within K Stops

[787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

**Solution**

Use a priority queue to store the shortest path so far. Need to reconstruct the graph so that it is easier for later BFS.

```python
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, K: int) -> int:
        edges = defaultdict(dict)
        graph = defaultdict(list)
        for flight in flights:
            edges[flight[0]][flight[1]] = flight[2]
            graph[flight[0]].append(flight[1])
        q = [(0, src, 0)]
        heapq.heapify(q)

        while q:
            cost, city, step = heapq.heappop(q)
            if city == dst:
                return cost
            if step > K:
                continue
            for next_stop in graph[city]:
                heapq.heappush(
                    q, (cost + edges[city][next_stop], next_stop, step + 1))
        return -1
```

## Jump Game III

[1306. Jump Game III](https://leetcode.com/problems/jump-game-iii/)

```python
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
```

## Open the Lock

[752. Open the Lock](https://leetcode.com/problems/open-the-lock/)

**Solution**

BFS, each time for the digits, scroll up or down.

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        q = deque([(0, '0000')])
        visited = {'0000'} | deadends

        while q:
            turns, state = q.popleft()
            if state == target:
                return turns
            for i in range(4):
                for direction in [1, -1]:
                    next_state = state[:i] + str(
                        (int(state[i]) + direction) % 10) + state[i + 1:]
                    if next_state not in visited:
                        q.append((turns + 1, next_state))
                        visited.add(next_state)
        return -1
```

## The Maze

[490. The Maze](https://leetcode.com/problems/the-maze/)

**Solution**

常规 BFS，注意这题每次滚动只有滚到墙了才能停下来，然后判断 wall 的时候注意考虑边界条件。

```python
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        q = deque([start])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            pos = q.popleft()

            if pos == destination:
                return True

            if tuple(pos) in visited:
                continue

            visited.add(tuple(pos))

            for i, j in directions:
                nx, ny = pos[0], pos[1]

                while 0 <= nx + i < m and 0 <= ny + j < n and maze[nx + i][ny + j] != 1:
                    nx, ny = nx + i, ny + j
                q.append([nx, ny])
        return False
```

## The Maze II

[505. The Maze II](https://leetcode.com/problems/the-maze-ii/)

**Solution**

Use priority queue.

```python
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
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

                while 0 <= nx + i < m and 0 <= ny + j < n and maze[nx + i][ny + j] != 1:
                    nx, ny = nx + i, ny + j
                    next_steps += 1

                heapq.heappush(q, (next_steps, nx, ny))

        return -1
```

## Trapping Rain Water II

[407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

**Solution**

Use priority queue. Starting from the boundaries, store each point on the boundaries into the queue. Each element in the queue would be a tuple of `(h, x, y)` where h is the water level for target spot, `x, y` is the position.

```python
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
```

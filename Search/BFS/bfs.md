# BFS

- [Is Graph Bipartite?](#is-graph-bipartite?)
- [Swim in Rising Water](#swim-in-rising-water)
- [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
- [Jump Game III](#jump-game-iii)
- [Open the Lock](#open-the-lock)
- [The Maze](#the-maze)
- [The Maze II](#the-maze-ii)
- [Trapping Rain Water II](#trapping-rain-water-ii)
- [Jump Game IV](#jump-game-iv)
- [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](#minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix)
- [Cut Off Trees for Golf Event](#cut-off-trees-for-golf-event)
- [Snakes and Ladders](#snakes-and-ladders)

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

## Jump Game IV

[1345. Jump Game IV](https://leetcode.com/problems/jump-game-iv/)

**Solution**

正常 BFS，这题有个 corner case，如果不处理会 TLE。就是如果同一个 val 每个 index 入 queue 以后记得避免`val_to_pos[val]`那个 list 被重复 iterate。

```python
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
```

## Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

[1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

**Solution**

这题较难，需要用到 bitmask 的思想，将矩阵 mat 压缩成一个 integer，然后每次对于每个位置做一个五点(cur, up, down, left, right)的 flip。其余思想就是一个 bfs。

```python
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
```

## Cut Off Trees for Golf Event

[675. Cut Off Trees for Golf Event](https://leetcode.com/problems/cut-off-trees-for-golf-event/)

**Solution**

这题难点在于 BFS 是用来算每一次从当前 node 走到目标 tree 的步长的。
最外层的 while loop 是基于存了所有待砍树的 Priority Queue，因为目标是砍完所有的树，所以 while loop 结束的条件是所有的树都砍光，或者出现有树没办法砍到。

```python
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
```

## Snakes and Ladders

[909. Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/)

**Solution**

比较需要注意的地方是根据x推r, c. 以及从board上取值下来要注意-1，因为x是从0开始算的。

```python
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        visited = set()
        # dq: each element is a pair of (steps, x) where x means the x-th
        # square.
        dq = deque([(0, 0)])

        while dq:
            steps, x = dq.popleft()

            if x == n ** 2 - 1:
                return steps

            if x in visited:
                continue

            visited.add(x)


            for i in range(1, 7):
                if x + i < n ** 2:
                    nx = x + i

                    # Be careful about the r, c computing
                    r = n - nx // n - 1
                    c = nx % n if (nx // n % 2 == 0) else n - nx % n - 1

                    if board[r][c] != -1:
                        # nx starts from 0, so we need to offset -1 for it.
                        nx = board[r][c] - 1

                    dq.append((steps + 1, nx))

        return -1
```

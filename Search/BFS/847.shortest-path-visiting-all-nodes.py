#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        q = deque([((1 << i), i) for i in range(n)])
        visited = set([((1 << i), i) for i in range(n)])

        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                status, node = q.popleft()

                if status == 2 ** n - 1:
                    return steps

                for next_node in graph[node]:
                    next_status = status
                    next_status |= (1 << next_node)
                    if (next_status, next_node) not in visited:
                        q.append((next_status, next_node))
                        visited.add((next_status, next_node))
            steps += 1




# @lc code=end


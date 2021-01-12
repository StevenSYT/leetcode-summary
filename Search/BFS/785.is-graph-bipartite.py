#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    # BFS 
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

    # DFS
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


# @lc code=end

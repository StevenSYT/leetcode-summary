#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        def dfs(node):
            for end in graph[node]:
                if end in colors:
                    if colors[end] != 1 - colors[node]:
                        return False
                else:
                    colors[end] = 1 - colors[node]
                    if not dfs(end):
                        return False
            return True

        for node in range(len(graph)):
            if node not in colors:
                colors[node] = 0
                if not dfs(node):
                    return False
        return True
# @lc code=end


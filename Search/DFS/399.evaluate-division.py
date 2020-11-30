#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        
        # Build graph: using zip can bring convenience.
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[x][y] = 1 / v
        
        # Process queries
        res = []
        for q1, q2 in queries:
            res.append(self.dfs(graph, q1, q2, {}))
        return res
    
    # TC: O(|V| * |E|)   [Ideally should be much smaller though]
    def dfs(self, graph, cur_node, target, seen):
        if cur_node not in graph or target not in graph:
            return -1
            
        if target in graph[cur_node]:
            return graph[cur_node][target]
        
        seen.add(cur_node)
        for next_node, val in list(graph[cur_node].items()):
            if next_node not in seen:
                res = self.dfs(graph, next_node, target, seen) * val
                if res >= 0:
                    return res
        return -1


# @lc code=end

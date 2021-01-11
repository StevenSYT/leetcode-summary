#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start

# Djikstra always start with the element with minimum time.
# Use a priority queue.
# Time: O(Vlog(V) + E)
# 再研究一下Bellman-Ford的解法：
# https://leetcode.com/problems/network-delay-time/discuss/109982/C%2B%2B-Bellman-Ford
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        q = [(0, K)]
        heapq.heapify(q)

        visited = set()
        res = 0
        while q:
            # 用pq，这样每一次总是从time最小的path往下延伸
            time, node = heapq.heappop(q)
            visited.add(node)
            res = time
            if len(visited) == N:
                return res
            for next_node in graph[node].keys():
                if next_node not in visited:
                    heapq.heappush(q,
                                   (time + graph[node][next_node], next_node))
        return -1


# @lc code=end

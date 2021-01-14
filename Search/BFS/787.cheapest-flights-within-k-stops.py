#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
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


# @lc code=end

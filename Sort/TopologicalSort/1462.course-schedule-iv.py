#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite1(self, n: int, prerequisites: List[List[int]],
                             queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for first, second in prerequisites:
            graph[first].append(second)
        res = []
        cache = {}
        for first, second in queries:
            res.append(self.dfs(first, second, graph, cache))
        return res

    # DFS + memo
    def dfs(self, first, second, graph, cache):
        if (first, second) in cache:
            return cache[first, second]

        if first == second:
            return True

        for next_node in graph[first]:
            if self.dfs(next_node, second, graph, cache):
                cache[first, second] = True
                return True
        cache[first, second] = False
        return False

    # Solution 2:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        # The direct graph where prerequisites point to courses.
        graph = defaultdict(list)
        indegree = [0] * n

        # Lookup table for each course, find its prerequisites.
        course_to_pre = defaultdict(set)

        # Construct the graph and the lookup table
        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            course_to_pre[course].add(pre)
        q = deque([node for node in range(n) if indegree[node] == 0])

        while q:
            pre = q.popleft()
            for course in graph[pre]:
                indegree[course] -= 1
                # The [pre]'s prerequisites are [course]'s prerequisites as well.
                course_to_pre[course] |= course_to_pre[pre]
                if indegree[course] == 0:
                    q.append(course)

        return [first in course_to_pre[second] for first, second in queries]


# @lc code=end

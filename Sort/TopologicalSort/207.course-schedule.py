#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        # Topological sort:
        # 1. Find the node with 0 indegree
        # 2. Remove the node from the graph and the edges: update the indegree of
        # the dependent
        # 3. Repeat 1 and 2 until there is no node in the graph or no node with
        # 0 indegree (The second situation means the graph is not a DAG).
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for first, second in prerequisites:
            graph[first].append(second)
            indegree[second] += 1
        q = deque(
            [course for course in range(numCourses) if indegree[course] == 0])
        while q:
            course = q.popleft()
            for dependent in graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        return sum(indegree) == 0


# @lc code=end

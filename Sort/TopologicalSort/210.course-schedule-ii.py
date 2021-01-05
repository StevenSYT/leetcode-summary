#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        # graph stores k, v pair where key is the prerequisite and value is
        # a list of dependents of that course
        #
        # indegrees stores the indegree of each course
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for first, second in prerequisites:
            graph[second].append(first)
            indegrees[first] += 1

        # Topological sort: start with the nodes with 0 indegree
        q = deque(
            [course for course in range(numCourses) if indegrees[course] == 0])

        # BFS remove 0 indegree nodes and the outgoing edges for each iteration.
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for dependent in graph[course]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    q.append(dependent)
        # This for loop is necessary for checking whether there is still non-zero indegree node.
        for indegree in indegrees:
            if indegree != 0:
                return []
        return res


# @lc code=end

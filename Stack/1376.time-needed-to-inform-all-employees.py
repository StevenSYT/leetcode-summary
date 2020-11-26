#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#


# @lc code=start
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int],
                     informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for reporter, m in enumerate(manager):
            graph[m].append(reporter)
        q = collections.deque([(headID, informTime[headID])])
        res = 0
        # Need to track the current time the message is passed to target person.
        while q:
            boss, cur_time = q.popleft()
            res = max(res, cur_time)
            for reporter in graph[boss]:
                q.append((reporter, cur_time + informTime[reporter]))

        return res


# @lc code=end

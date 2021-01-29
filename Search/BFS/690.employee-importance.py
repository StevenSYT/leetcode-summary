#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dq = deque([id])
        em_map = {e.id: e for e in employees}
        res = 0
        while dq:
            em_id = dq.popleft()
            res += em_map[em_id].importance

            for subordinate in em_map[em_id].subordinates:
                dq.append(subordinate)
        return res


# @lc code=end

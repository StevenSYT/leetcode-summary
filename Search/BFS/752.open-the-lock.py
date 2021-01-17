#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        q = deque([(0, '0000')])
        visited = {'0000'} | deadends

        while q:
            turns, state = q.popleft()
            if state == target:
                return turns
            for i in range(4):
                for direction in [1, -1]:
                    next_state = state[:i] + str(
                        (int(state[i]) + direction) % 10) + state[i + 1:]
                    if next_state not in visited:
                        q.append((turns + 1, next_state))
                        visited.add(next_state)
        return -1


# @lc code=end

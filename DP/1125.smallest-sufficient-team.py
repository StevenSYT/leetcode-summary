#
# @lc app=leetcode id=1125 lang=python3
#
# [1125] Smallest Sufficient Team
#

# @lc code=start
from collections import deque
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        queue = deque([(set(req_skills), set())])

        while queue:
            target_skills, cur_team = queue.popleft()
            for idx, person in enumerate(people):
                if idx in cur_team:
                    continue
                # We need solve/remove all skills in the skillset,
                # so why not just only care about people who has
                # the first skill in target_skills.
                # note that since we cannot index through set, we need
                # to use this next(iter(S)) to access one item in set.
                # TC for next(iter(S)) is O(1) --- needs confirmation.
                if next(iter(target_skills)) not in person:
                    continue
                next_target = target_skills.copy()
                for skill in person:
                    if skill in next_target:
                        next_target.remove(skill)
                if len(next_target) == 0:
                    return cur_team | {idx}
                queue.append((next_target, cur_team | {idx}))
                
# @lc code=end

